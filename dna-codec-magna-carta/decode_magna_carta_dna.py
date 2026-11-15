#!/usr/bin/env python3
"""
Independent decoder for the Magna Carta DNA lane.
Written from the written specification alone (2026-11-14).

Specification implemented:
- Sequence file: magna-carta-dna.txt — base stream wrapped at 60 bases
  per line; strip all whitespace.
- Codec: each base is two bits — A=00, C=01, G=10, T=11.
  Four bases make one byte, most significant pair first.
- Source file: magna-carta-1215-latin-source.txt
- Manifest: MANIFEST-DNA-MAGNA-CARTA.md containing lines of the form
  "SHA-256 of the source byte stream: `<hex>`" and
  "SHA-256 of the base stream: `<hex>`"
  (base-stream hash over the stripped base stream's ASCII bytes).
- Expected base count: 99320.
"""

import hashlib
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SEQ_PATH = BASE_DIR / "magna-carta-dna.txt"
SRC_PATH = BASE_DIR / "magna-carta-1215-latin-source.txt"
MANIFEST_PATH = BASE_DIR / "MANIFEST-DNA-MAGNA-CARTA.md"
EXPECTED_BASE_COUNT = 99320

# --- Primary decoder: table-driven, per spec A=00, C=01, G=10, T=11 ---
BASE_TO_BITS = {
    "A": 0b00,
    "C": 0b01,
    "G": 0b10,
    "T": 0b11,
}


def decode_base_stream(bases: str) -> bytes:
    """Decode a stripped base string to bytes.

    Four bases make one byte, most significant pair first:
    byte = (b0 << 6) | (b1 << 4) | (b2 << 2) | b3
    where each bi is the two-bit value of the base.
    """
    if len(bases) % 4 != 0:
        raise ValueError(f"Base count {len(bases)} is not divisible by 4")
    out = bytearray()
    for i in range(0, len(bases), 4):
        quad = bases[i : i + 4]
        value = 0
        for ch in quad:
            if ch not in BASE_TO_BITS:
                raise ValueError(f"Invalid base {ch!r} at position {i}")
            value = (value << 2) | BASE_TO_BITS[ch]
        out.append(value)
    return bytes(out)


# --- Independent re-encoder: separately written, bit-extraction logic ---
# This does NOT reuse BASE_TO_BITS or the decoder's grouping logic.
# It extracts two bits at a time from each byte by shifting/masking,
# and maps the integer 0..3 to a base via an indexed tuple.
BITS_TO_BASE = ("A", "C", "G", "T")


def re_encode_bytes(data: bytes) -> str:
    parts = []
    for byte in data:
        # Most significant pair first: shifts 6, 4, 2, 0
        for shift in (6, 4, 2, 0):
            pair = (byte >> shift) & 0b11
            parts.append(BITS_TO_BASE[pair])
    return "".join(parts)


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
    seq_raw = SEQ_PATH.read_text(encoding="ascii")
    # Strip all whitespace per spec
    bases = "".join(seq_raw.split())
    # Also equivalent: re.sub(r"\s+", "", seq_raw)

    source_bytes = SRC_PATH.read_bytes()
    manifest_text = MANIFEST_PATH.read_text(encoding="utf-8")

    manifest_src_hash, manifest_base_hash = parse_manifest_hashes(manifest_text)

    # Figures
    total_bases = len(bases)
    alphabet = sorted(set(bases))
    alphabet_set = set(bases)

    decoded_bytes = b""
    decode_error = None
    try:
        decoded_bytes = decode_base_stream(bases)
    except Exception as e:
        decode_error = str(e)

    sha_decoded = hashlib.sha256(decoded_bytes).hexdigest() if decoded_bytes else None
    sha_source = hashlib.sha256(source_bytes).hexdigest()
    sha_bases = hashlib.sha256(bases.encode("ascii")).hexdigest()

    print(f"Total bases: {total_bases}")
    print(f"Expected base count: {EXPECTED_BASE_COUNT}")
    print(f"Alphabet: {alphabet}")
    print(f"Decoded bytes: {len(decoded_bytes)}")
    print(f"Source bytes: {len(source_bytes)}")
    print(f"SHA-256 of decoded stream: {sha_decoded}")
    print(f"SHA-256 of source (computed): {sha_source}")
    print(f"SHA-256 of base stream (computed): {sha_bases}")
    print(f"SHA-256 of source (manifest): {manifest_src_hash}")
    print(f"SHA-256 of base stream (manifest): {manifest_base_hash}")
    if decode_error:
        print(f"Decode error: {decode_error}")

    # (a) base count == 99320, alphabet exactly {A,C,G,T}, count divisible by 4
    check_a = (
        total_bases == EXPECTED_BASE_COUNT
        and alphabet_set == {"A", "C", "G", "T"}
        and total_bases % 4 == 0
    )
    print(f"\n(a) base count / alphabet / divisible-by-4: {'PASS' if check_a else 'FAIL'}")

    # (b) full decode is valid UTF-8
    check_b = False
    utf8_error = None
    try:
        decoded_bytes.decode("utf-8")
        check_b = True
    except UnicodeDecodeError as e:
        utf8_error = str(e)
    print(f"(b) valid UTF-8: {'PASS' if check_b else 'FAIL'} {utf8_error or ''}")

    # (c) decoded == source byte-for-byte, and SHA(decoded) == SHA(source)
    check_c = (decoded_bytes == source_bytes) and (sha_decoded == sha_source)
    print(f"(c) decoded == source and SHA match: {'PASS' if check_c else 'FAIL'}")

    # (d) both manifest SHA figures match computed
    check_d = (manifest_src_hash == sha_source) and (manifest_base_hash == sha_bases)
    print(f"(d) manifest hashes match computed: {'PASS' if check_d else 'FAIL'}")

    # (e) spot proofs with independent re-encoder
    n = len(source_bytes)
    chunks = []
    # first 1000
    chunks.append(("first", 0, source_bytes[0:1000]))
    # centered on midpoint
    mid = n // 2
    mid_start = mid - 500
    chunks.append(("midpoint", mid_start, source_bytes[mid_start : mid_start + 1000]))
    # last 1000
    last_start = n - 1000
    chunks.append(("last", last_start, source_bytes[last_start : last_start + 1000]))

    check_e = True
    for label, offset, chunk in chunks:
        re_encoded = re_encode_bytes(chunk)
        seq_slice = bases[offset * 4 : (offset + len(chunk)) * 4]
        ok = re_encoded == seq_slice
        print(
            f"(e) spot {label}: offset={offset} len={len(chunk)} "
            f"seq_offset={offset * 4} match={ok} {'PASS' if ok else 'FAIL'}"
        )
        if not ok:
            check_e = False

    print(f"(e) spot proofs overall: {'PASS' if check_e else 'FAIL'}")

    all_pass = check_a and check_b and check_c and check_d and check_e
    print(f"\nVERDICT: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
