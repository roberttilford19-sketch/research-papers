#!/usr/bin/env python3
"""
Independent decoder for the Gettysburg Address DNA lane.
Written from the written specification alone (2026-11-14).

Codec (from spec):
  Each base is two bits -- A=00, C=01, G=10, T=11.
  Four bases make one byte, most significant pair first.
  Sequence file is wrapped at 60 bases per line; strip all whitespace.
  Expected base count: 5876.
"""

import hashlib
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SEQ_PATH = BASE_DIR / "gettysburg-dna.txt"
SRC_PATH = BASE_DIR / "gettysburg-address-source.txt"
MANIFEST_PATH = BASE_DIR / "MANIFEST-DNA-GETTYSBURG.md"
EXPECTED_BASE_COUNT = 5876

# --- Decoder: base -> 2-bit value via explicit mapping, byte assembled by shifts ---
BASE_TO_BITS = {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}


def decode_bases(bases: str) -> bytes:
    """Decode a base string to bytes: 4 bases per byte, MSB pair first."""
    if len(bases) % 4 != 0:
        raise ValueError(f"base count {len(bases)} not divisible by 4")
    out = bytearray()
    for i in range(0, len(bases), 4):
        byte_val = 0
        for j in range(4):
            base = bases[i + j]
            if base not in BASE_TO_BITS:
                raise ValueError(f"invalid base {base!r} at position {i + j}")
            byte_val = (byte_val << 2) | BASE_TO_BITS[base]
        out.append(byte_val)
    return bytes(out)


# --- Re-encoder: SEPARATELY written, independent bit-extraction logic ---
# This implementation does NOT reuse BASE_TO_BITS or shift assembly.
# It converts each byte to an 8-character binary string via format(),
# slices it into 2-character chunks, and maps chunk strings to bases.
_BITS_TO_BASE = {"00": "A", "01": "C", "10": "G", "11": "T"}


def re_encode_bytes(data: bytes) -> str:
    parts = []
    for b in data:
        bitstring = format(b, "08b")  # independent extraction: textual bits
        for k in (0, 2, 4, 6):
            parts.append(_BITS_TO_BASE[bitstring[k : k + 2]])
    return "".join(parts)


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_manifest_hashes(manifest_text: str):
    src_match = re.search(
        r"SHA-256 of the source byte stream:\s*`([0-9a-fA-F]+)`", manifest_text
    )
    base_match = re.search(
        r"SHA-256 of the base stream:\s*`([0-9a-fA-F]+)`", manifest_text
    )
    src_hash = src_match.group(1).lower() if src_match else None
    base_hash = base_match.group(1).lower() if base_match else None
    return src_hash, base_hash


def main() -> int:
    # Load inputs
    seq_raw = SEQ_PATH.read_bytes()
    # Strip all whitespace per spec
    bases = "".join(seq_raw.decode("ascii").split())
    source_bytes = SRC_PATH.read_bytes()
    manifest_text = MANIFEST_PATH.read_text(encoding="utf-8")

    manifest_src_hash, manifest_base_hash = parse_manifest_hashes(manifest_text)

    # Decode
    decoded_bytes = decode_bases(bases)

    # Computed figures
    total_bases = len(bases)
    alphabet = sorted(set(bases))
    decoded_len = len(decoded_bytes)
    source_len = len(source_bytes)
    sha_decoded = sha256_hex(decoded_bytes)
    sha_source = sha256_hex(source_bytes)
    sha_bases = sha256_hex(bases.encode("ascii"))

    print(f"Total bases: {total_bases}")
    print(f"Expected base count: {EXPECTED_BASE_COUNT}")
    print(f"Alphabet: {alphabet}")
    print(f"Decoded bytes: {decoded_len}")
    print(f"Source bytes: {source_len}")
    print(f"SHA-256 decoded: {sha_decoded}")
    print(f"SHA-256 source (computed): {sha_source}")
    print(f"SHA-256 base stream (computed): {sha_bases}")
    print(f"SHA-256 source (manifest): {manifest_src_hash}")
    print(f"SHA-256 base stream (manifest): {manifest_base_hash}")

    checks = {}

    # (a) base count == 5876, alphabet exactly {A,C,G,T}, count divisible by 4
    check_a = (
        total_bases == EXPECTED_BASE_COUNT
        and set(bases) == {"A", "C", "G", "T"}
        and total_bases % 4 == 0
    )
    checks["a"] = check_a
    print(f"(a) base count/alphabet/divisible-by-4: {'PASS' if check_a else 'FAIL'}")

    # (b) full decode is valid UTF-8
    try:
        decoded_bytes.decode("utf-8")
        check_b = True
    except UnicodeDecodeError as e:
        check_b = False
        print(f"    UTF-8 error: {e}")
    checks["b"] = check_b
    print(f"(b) valid UTF-8: {'PASS' if check_b else 'FAIL'}")

    # (c) decoded == source byte-for-byte, and SHA-256(decoded) == SHA-256(source)
    check_c = (decoded_bytes == source_bytes) and (sha_decoded == sha_source)
    checks["c"] = check_c
    print(f"(c) decoded == source and hashes match: {'PASS' if check_c else 'FAIL'}")

    # (d) both manifest SHA-256 figures match computed values
    check_d = (manifest_src_hash == sha_source) and (manifest_base_hash == sha_bases)
    checks["d"] = check_d
    print(f"(d) manifest hashes match computed: {'PASS' if check_d else 'FAIL'}")

    # (e) spot proofs: re-encode first 300, middle 300 centered on midpoint, last 300
    n = source_len
    mid_start = n // 2 - 150
    chunks = [
        ("first 300", 0, source_bytes[0:300]),
        ("middle 300 (centered)", mid_start, source_bytes[mid_start : mid_start + 300]),
        ("last 300", n - 300, source_bytes[n - 300 : n]),
    ]
    check_e = True
    for label, offset, chunk in chunks:
        reencoded = re_encode_bytes(chunk)
        seq_slice = bases[offset * 4 : (offset + len(chunk)) * 4]
        ok = reencoded == seq_slice
        print(
            f"    spot {label}: byte offset {offset}, bytes {len(chunk)}, "
            f"bases {len(reencoded)} vs seq slice {len(seq_slice)}: "
            f"{'PASS' if ok else 'FAIL'}"
        )
        if not ok:
            check_e = False
    checks["e"] = check_e
    print(f"(e) spot proofs: {'PASS' if check_e else 'FAIL'}")

    all_pass = all(checks.values())
    print(f"VERDICT: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
