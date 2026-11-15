#!/usr/bin/env python3
"""
Independent decoder for the U.S. Constitution DNA lane.
Written from the specification alone (2026-11-14).

Codec (from specification):
  Each byte -> 8 bits, most significant bit first -> the 8 bits are split
  into four pairs -> each pair maps to one base: 00=A, 01=C, 10=G, 11=T.
  So one byte = four bases.
  Decoding is the exact inverse: A=00, C=01, G=10, T=11,
  four bases make one byte, most significant pair first.

Sequence file: constitution-dna-full.txt wrapped at 60 bases per line;
strip all whitespace before decoding.
"""

import hashlib
import pathlib
import sys

BASE_DIR = pathlib.Path(__file__).resolve().parent
SEQ_PATH = BASE_DIR / "constitution-dna-full.txt"
SRC_PATH = BASE_DIR / "us-constitution-nara-transcription.txt"

# Manifest figures (copied from MANIFEST-DNA-FULL-CONSTITUTION.md)
MANIFEST_SOURCE_SHA256 = "5ba284d94d3f768de194b425edd4b48ca4ff65c7708d1fe454e4ef3d82899b07"
MANIFEST_BASE_SHA256 = "880e1058450f558eee9c264490307c475648034314aeee29b569225e4511ffd1"

# --- Decoder (spec inverse) ---
BASE_TO_PAIR = {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}


def decode_bases(base_stream: str) -> bytes:
    """Decode a string of A/C/G/T bases to bytes, 4 bases per byte, MSB pair first."""
    if len(base_stream) % 4 != 0:
        raise ValueError(f"Base count {len(base_stream)} is not divisible by 4")
    out = bytearray()
    for i in range(0, len(base_stream), 4):
        b = 0
        for j in range(4):
            ch = base_stream[i + j]
            if ch not in BASE_TO_PAIR:
                raise ValueError(f"Invalid base {ch!r} at position {i + j}")
            b = (b << 2) | BASE_TO_PAIR[ch]
        out.append(b)
    return bytes(out)


# --- Separate re-encoder (independent logic: bit-mask extraction) ---
# Deliberately written differently from the decoder: for each byte, extract
# the four 2-bit fields by shifting/masking (bits 7-6, 5-4, 3-2, 1-0) and
# index into a tuple. No shared table with the decoder's dict logic path.
_PAIR_TO_BASE = ("A", "C", "G", "T")


def reencode_bytes(data: bytes) -> str:
    parts = []
    for byte in data:
        parts.append(_PAIR_TO_BASE[(byte >> 6) & 0b11])
        parts.append(_PAIR_TO_BASE[(byte >> 4) & 0b11])
        parts.append(_PAIR_TO_BASE[(byte >> 2) & 0b11])
        parts.append(_PAIR_TO_BASE[byte & 0b11])
    return "".join(parts)


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    seq_raw = SEQ_PATH.read_text(encoding="utf-8")
    # Strip all whitespace before decoding, per specification.
    base_stream = "".join(seq_raw.split())
    source_bytes = SRC_PATH.read_bytes()

    total_bases = len(base_stream)
    alphabet = sorted(set(base_stream))
    alphabet_str = "{" + ",".join(alphabet) + "}"

    decoded_bytes = decode_bases(base_stream)

    decoded_sha = sha256_hex(decoded_bytes)
    source_sha = sha256_hex(source_bytes)
    base_sha = sha256_hex(base_stream.encode("ascii"))

    print(f"total_bases: {total_bases}")
    print(f"alphabet: {alphabet_str}")
    print(f"decoded_bytes: {len(decoded_bytes)}")
    print(f"source_bytes: {len(source_bytes)}")
    print(f"sha256_decoded: {decoded_sha}")
    print(f"sha256_source: {source_sha}")
    print(f"sha256_base_stream: {base_sha}")
    print(f"manifest_sha256_source: {MANIFEST_SOURCE_SHA256}")
    print(f"manifest_sha256_base_stream: {MANIFEST_BASE_SHA256}")

    # Check (a)
    check_a_count = total_bases == 4 * len(source_bytes)
    check_a_alpha = set(base_stream) == {"A", "C", "G", "T"}
    check_a_div4 = (total_bases % 4 == 0)
    check_a = check_a_count and check_a_alpha and check_a_div4
    print(f"check_a_base_count_equals_4x_source: {check_a_count} ({total_bases} vs {4 * len(source_bytes)})")
    print(f"check_a_alphabet_exactly_ACGT: {check_a_alpha}")
    print(f"check_a_divisible_by_4: {check_a_div4}")
    print(f"check_a: {'PASS' if check_a else 'FAIL'}")

    # Check (b)
    try:
        decoded_bytes.decode("utf-8")
        check_b = True
    except UnicodeDecodeError as e:
        check_b = False
        print(f"utf8_error: {e}")
    print(f"check_b_valid_utf8: {'PASS' if check_b else 'FAIL'}")

    # Check (c)
    check_c_bytes = decoded_bytes == source_bytes
    check_c_hash = decoded_sha == source_sha
    check_c = check_c_bytes and check_c_hash
    print(f"check_c_bytes_equal: {check_c_bytes}")
    print(f"check_c_sha_equal: {check_c_hash}")
    print(f"check_c: {'PASS' if check_c else 'FAIL'}")

    # Check (d)
    check_d_source = (MANIFEST_SOURCE_SHA256 == source_sha)
    check_d_base = (MANIFEST_BASE_SHA256 == base_sha)
    check_d = check_d_source and check_d_base
    print(f"check_d_manifest_source_match: {check_d_source}")
    print(f"check_d_manifest_base_match: {check_d_base}")
    print(f"check_d: {'PASS' if check_d else 'FAIL'}")

    # Check (e) spot proofs with independent re-encoder
    n = len(source_bytes)
    mid_start = n // 2 - 500
    slices = [
        ("first_1000", 0, source_bytes[0:1000]),
        ("middle_1000_centered", mid_start, source_bytes[mid_start:mid_start + 1000]),
        ("last_1000", n - 1000, source_bytes[n - 1000:n]),
    ]
    all_spot = True
    for name, byte_offset, chunk in slices:
        reencoded = reencode_bytes(chunk)
        base_offset = byte_offset * 4
        expected = base_stream[base_offset:base_offset + len(reencoded)]
        ok = (reencoded == expected)
        all_spot = all_spot and ok
        print(f"spot_{name}: byte_offset={byte_offset} base_offset={base_offset} length_bytes={len(chunk)} match={ok} {'PASS' if ok else 'FAIL'}")
    check_e = all_spot
    print(f"check_e: {'PASS' if check_e else 'FAIL'}")

    overall = check_a and check_b and check_c and check_d and check_e
    print(f"VERDICT: {'PASS' if overall else 'FAIL'}")
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
