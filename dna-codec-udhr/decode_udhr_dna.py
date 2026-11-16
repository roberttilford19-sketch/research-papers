#!/usr/bin/env python3
"""
Independent decoder for the UDHR DNA lane.
Written from the written specification alone (2026-11-15).

Spec:
- Sequence file holds base stream wrapped at 60 bases per line; strip whitespace.
- Each base is two bits: A=00, C=01, G=10, T=11.
- Four bases make one byte, most significant pair first.
- Decoded byte stream should equal the lane's source file bytes.
"""
import sys
import os
import hashlib
import re

DEFAULT_SOURCE = os.path.expanduser("~/workspace/dna-udhr-2026-11-15/udhr-un-official-text.txt")
SEQUENCE_PATH = os.path.expanduser("~/workspace/dna-udhr-2026-11-15/udhr-dna-full.txt")
MANIFEST_PATH = os.path.expanduser("~/workspace/dna-udhr-2026-11-15/MANIFEST-DNA-FULL-UDHR.md")

EXPECTED_BASE_COUNT = 43284

BASE_TO_BITS = {
    'A': 0b00,
    'C': 0b01,
    'G': 0b10,
    'T': 0b11,
}

BITS_TO_BASE = {
    0b00: 'A',
    0b01: 'C',
    0b10: 'G',
    0b11: 'T',
}


def load_base_stream(path):
    with open(path, 'r', encoding='ascii') as f:
        raw = f.read()
    return ''.join(raw.split())


def decode_bases(base_str):
    """Decode base string to bytes: 4 bases -> 1 byte, MSB pair first."""
    if len(base_str) % 4 != 0:
        raise ValueError(f"Base count {len(base_str)} not divisible by 4")
    out = bytearray()
    for i in range(0, len(base_str), 4):
        chunk = base_str[i:i+4]
        b = 0
        for j, ch in enumerate(chunk):
            if ch not in BASE_TO_BITS:
                raise ValueError(f"Invalid base {ch!r} at position {i+j}")
            shift = (3 - j) * 2
            b |= (BASE_TO_BITS[ch] << shift)
        out.append(b)
    return bytes(out)


def encode_bytes_independent(data):
    """Separately-written re-encoder for spot proofs (mask extraction)."""
    result_chars = []
    for byte_val in data:
        for shift in (6, 4, 2, 0):
            pair = (byte_val >> shift) & 0b11
            result_chars.append(BITS_TO_BASE[pair])
    return ''.join(result_chars)


def sha256_hex(data_bytes):
    return hashlib.sha256(data_bytes).hexdigest()


def parse_manifest(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    source_match = re.search(r"SHA-256 of the source byte stream:\s*`([0-9a-fA-F]{64})`", text)
    base_match = re.search(r"SHA-256 of the base stream:\s*`([0-9a-fA-F]{64})`", text)
    source_sha = source_match.group(1).lower() if source_match else None
    base_sha = base_match.group(1).lower() if base_match else None
    return source_sha, base_sha


def main():
    source_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SOURCE

    print(f"Source path: {source_path}")
    print(f"Sequence path: {SEQUENCE_PATH}")
    print(f"Manifest path: {MANIFEST_PATH}")

    base_str = load_base_stream(SEQUENCE_PATH)
    base_count = len(base_str)
    alphabet = set(base_str)
    print(f"Base count: {base_count}")
    print(f"Alphabet: {sorted(alphabet)}")
    print(f"Divisible by 4: {base_count % 4 == 0} (remainder {base_count % 4})")

    check_a = (base_count == EXPECTED_BASE_COUNT and alphabet == {'A', 'C', 'G', 'T'} and base_count % 4 == 0)
    print(f"Check (a) base count/alphabet/divisible: {'PASS' if check_a else 'FAIL'}")

    decoded = decode_bases(base_str)
    print(f"Decoded bytes: {len(decoded)}")

    try:
        decoded.decode('utf-8')
        utf8_ok = True
    except UnicodeDecodeError as e:
        utf8_ok = False
        print(f"UTF-8 error: {e}")
    print(f"Check (b) valid UTF-8: {'PASS' if utf8_ok else 'FAIL'}")

    with open(source_path, 'rb') as f:
        source_bytes = f.read()
    print(f"Source bytes: {len(source_bytes)}")

    decoded_sha = sha256_hex(decoded)
    source_sha_computed = sha256_hex(source_bytes)
    base_sha_computed = sha256_hex(base_str.encode('ascii'))

    print(f"SHA-256 decoded: {decoded_sha}")
    print(f"SHA-256 source (computed): {source_sha_computed}")
    print(f"SHA-256 base stream (computed): {base_sha_computed}")

    equal_bytes = (decoded == source_bytes)
    sha_match_c = (decoded_sha == source_sha_computed)
    check_c = equal_bytes and sha_match_c
    print(f"Check (c) decoded == source and SHA match: {'PASS' if check_c else 'FAIL'} (equal={equal_bytes}, sha_match={sha_match_c})")

    manifest_source_sha, manifest_base_sha = parse_manifest(MANIFEST_PATH)
    print(f"Manifest source SHA: {manifest_source_sha}")
    print(f"Manifest base SHA: {manifest_base_sha}")
    check_d = (manifest_source_sha == source_sha_computed and manifest_base_sha == base_sha_computed)
    print(f"Check (d) manifest matches computed: {'PASS' if check_d else 'FAIL'}")

    total_len = len(source_bytes)
    spots = []
    spots.append(("first", 0, source_bytes[0:1000]))
    mid = total_len // 2
    mid_start = mid - 500
    spots.append(("middle", mid_start, source_bytes[mid_start:mid_start+1000]))
    last_start = total_len - 1000
    spots.append(("last", last_start, source_bytes[last_start:last_start+1000]))

    all_spots_pass = True
    for label, offset, chunk in spots:
        reencoded = encode_bytes_independent(chunk)
        seq_offset = offset * 4
        seq_slice = base_str[seq_offset:seq_offset + len(chunk)*4]
        match = (reencoded == seq_slice)
        print(f"Spot {label}: offset={offset}, bytes={len(chunk)}, base_offset={seq_offset}, match={match}")
        if not match:
            all_spots_pass = False

    check_e = all_spots_pass
    print(f"Check (e) spot proofs: {'PASS' if check_e else 'FAIL'}")

    all_pass = check_a and utf8_ok and check_c and check_d and check_e
    print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
