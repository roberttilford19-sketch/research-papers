#!/usr/bin/env python3
"""
Independent decoder for the I Ching draft DNA lane.

Written from the written specification alone (2026-11-14).
Specification summary implemented here:
  - Sequence file holds a base stream wrapped at 60 bases per line;
    strip all whitespace before decoding.
  - Each base is two bits: A=00, C=01, G=10, T=11.
  - Four bases make one byte, most significant pair first.
  - Decoded byte stream should equal the source assembly file exactly.
  - Manifest prints source and base-stream SHA-256 figures, and a
    component table with byte ranges (1-based inclusive) and SHA-256
    values for seven components.

Usage:
    python3 decode_iching_dna.py [source_path]

If source_path is omitted, it defaults to the assembly file beside
this script.
"""

import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEQUENCE_PATH = HERE / "iching-dna-full.txt"
MANIFEST_PATH = HERE / "MANIFEST-DNA-ICHING-DRAFT.md"
DEFAULT_SOURCE_PATH = HERE / "I-CHING-DRAFT-ASSEMBLY-352-OF-450.txt"

EXPECTED_BASE_COUNT = 1_104_764
EXPECTED_SOURCE_BYTES = 276_191

# --- Decoder (written from the specification) ---------------------------

# Two-bit value of each base, per the specification.
BASE_TO_BITS = {
    "A": 0b00,
    "C": 0b01,
    "G": 0b10,
    "T": 0b11,
}


def decode_bases(bases: str) -> bytes:
    """Decode a stripped base string to bytes.

    Groups of four bases form one byte; the first base in a group
    supplies the most significant two bits, the last the least.
    """
    if len(bases) % 4 != 0:
        raise ValueError(f"base count {len(bases)} is not divisible by 4")
    out = bytearray()
    for i in range(0, len(bases), 4):
        value = 0
        for base in bases[i : i + 4]:
            if base not in BASE_TO_BITS:
                raise ValueError(f"invalid base {base!r} at position {i}")
            value = (value << 2) | BASE_TO_BITS[base]
        out.append(value)
    return bytes(out)


# --- Re-encoder (separately written, for spot proofs only) ---------------

# Inverse table, indexed by the two-bit value 0..3.
BITS_TO_BASE = ("A", "C", "G", "T")


def encode_bytes(data: bytes) -> str:
    """Encode bytes to bases, most significant pair of each byte first."""
    pieces = []
    for byte in data:
        # Extract the four two-bit fields from high to low.
        pieces.append(BITS_TO_BASE[(byte >> 6) & 0b11])
        pieces.append(BITS_TO_BASE[(byte >> 4) & 0b11])
        pieces.append(BITS_TO_BASE[(byte >> 2) & 0b11])
        pieces.append(BITS_TO_BASE[byte & 0b11])
    return "".join(pieces)


# --- Manifest parsing -----------------------------------------------------

def parse_manifest(text: str):
    """Return (source_sha, base_sha, components).

    components is a list of dicts with keys: name, bytes, sha256,
    start, end (1-based inclusive byte range in the assembly).
    """
    source_match = re.search(
        r"SHA-256 of the source byte stream:\s*`([0-9a-fA-F]{64})`", text
    )
    base_match = re.search(
        r"SHA-256 of the base stream:\s*`([0-9a-fA-F]{64})`", text
    )
    source_sha = source_match.group(1).lower() if source_match else None
    base_sha = base_match.group(1).lower() if base_match else None

    components = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        # Component table has 8 columns; header and separator rows are
        # filtered by requiring a .md filename in column 1, a plain
        # integer byte count in column 5, and a 64-hex hash in column 6.
        if len(cells) != 8:
            continue
        name_match = re.search(r"`([^`]+\.md)`", cells[0])
        if not name_match:
            continue
        sha_match = re.search(r"`([0-9a-fA-F]{64})`", cells[5])
        if not sha_match:
            continue
        bytes_text = cells[4].replace(",", "").strip()
        if not bytes_text.isdigit():
            continue
        # Byte range uses an en dash (or hyphen) and thousands commas.
        range_text = cells[6].replace(",", "")
        range_match = re.search(r"(\d+)\s*[-\u2013\u2014]\s*(\d+)", range_text)
        if not range_match:
            continue
        components.append(
            {
                "name": name_match.group(1),
                "bytes": int(bytes_text),
                "sha256": sha_match.group(1).lower(),
                "start": int(range_match.group(1)),
                "end": int(range_match.group(2)),
            }
        )
    return source_sha, base_sha, components


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    source_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE_PATH

    # Load the sequence and strip all whitespace, per the specification.
    raw_sequence = SEQUENCE_PATH.read_bytes()
    bases = "".join(raw_sequence.decode("ascii").split())

    # Load the source of record.
    source_bytes = source_path.read_bytes()

    # Load and parse the manifest.
    manifest_text = MANIFEST_PATH.read_text(encoding="utf-8")
    manifest_source_sha, manifest_base_sha, components = parse_manifest(manifest_text)

    results = {}

    # (a) Base count, alphabet, divisibility by 4.
    alphabet = sorted(set(bases))
    check_a = (
        len(bases) == EXPECTED_BASE_COUNT
        and set(alphabet) == {"A", "C", "G", "T"}
        and len(bases) % 4 == 0
    )
    results["a"] = check_a
    print(f"base_count={len(bases)}")
    print(f"expected_base_count={EXPECTED_BASE_COUNT}")
    print(f"alphabet={','.join(alphabet)}")
    print(f"base_count_mod_4={len(bases) % 4}")
    print(f"check_a={'PASS' if check_a else 'FAIL'}")

    # Decode the full stream.
    decoded = decode_bases(bases)
    print(f"decoded_bytes={len(decoded)}")
    print(f"source_bytes={len(source_bytes)}")
    print(f"expected_source_bytes={EXPECTED_SOURCE_BYTES}")

    # (b) Full decode is valid UTF-8.
    try:
        decoded.decode("utf-8")
        utf8_ok = True
        utf8_error = ""
    except UnicodeDecodeError as exc:
        utf8_ok = False
        utf8_error = str(exc)
    results["b"] = utf8_ok
    print(f"utf8_valid={utf8_ok}")
    if utf8_error:
        print(f"utf8_error={utf8_error}")
    print(f"check_b={'PASS' if utf8_ok else 'FAIL'}")

    # Hashes computed by this decoder.
    source_sha = sha256_hex(source_bytes)
    decoded_sha = sha256_hex(decoded)
    base_sha = sha256_hex(bases.encode("ascii"))
    print(f"sha256_source={source_sha}")
    print(f"sha256_decoded={decoded_sha}")
    print(f"sha256_base_stream={base_sha}")
    print(f"manifest_sha256_source={manifest_source_sha}")
    print(f"manifest_sha256_base_stream={manifest_base_sha}")

    # (c) Decoded bytes equal the assembly byte-for-byte; hashes match.
    check_c = decoded == source_bytes and decoded_sha == source_sha
    results["c"] = check_c
    print(f"decoded_equals_source={decoded == source_bytes}")
    print(f"check_c={'PASS' if check_c else 'FAIL'}")

    # (d) Both manifest SHA-256 figures match computed values.
    check_d = manifest_source_sha == source_sha and manifest_base_sha == base_sha
    # Also require the manifest source figure to agree with the decoded hash.
    check_d = bool(check_d and manifest_source_sha == decoded_sha)
    results["d"] = check_d
    print(f"manifest_source_match={manifest_source_sha == source_sha}")
    print(f"manifest_base_match={manifest_base_sha == base_sha}")
    print(f"check_d={'PASS' if check_d else 'FAIL'}")

    # (e) Spot proofs: re-encode first / middle / last 1,000 source bytes
    # with the separately written re-encoder above and compare against
    # the corresponding slices of the sequence (byte offset x 4).
    n = len(source_bytes)
    midpoint = n // 2
    windows = [
        ("first", 0, 1000),
        ("middle", midpoint - 500, midpoint - 500 + 1000),
        ("last", n - 1000, n),
    ]
    spot_all = True
    for label, start, end in windows:
        chunk = source_bytes[start:end]
        reencoded = encode_bytes(chunk)
        sequence_slice = bases[start * 4 : end * 4]
        ok = reencoded == sequence_slice and len(chunk) == 1000
        spot_all = spot_all and ok
        print(
            f"spot_{label}=byte_range_{start}-{end - 1}_"
            f"bases_{start * 4}-{end * 4 - 1}_len_{len(chunk)}_"
            f"{'PASS' if ok else 'FAIL'}"
        )
    results["e"] = spot_all
    print(f"check_e={'PASS' if spot_all else 'FAIL'}")

    # (f) Component check: slice decoded bytes at each manifest byte
    # range (1-based inclusive), hash the slice, compare to the table.
    print(f"component_count={len(components)}")
    component_all = len(components) == 7
    for idx, comp in enumerate(components, start=1):
        # 1-based inclusive [start, end] -> python slice [start-1:end]
        piece = decoded[comp["start"] - 1 : comp["end"]]
        piece_sha = sha256_hex(piece)
        length_ok = len(piece) == comp["bytes"] and (
            comp["end"] - comp["start"] + 1
        ) == comp["bytes"]
        ok = piece_sha == comp["sha256"] and length_ok
        component_all = component_all and ok
        print(
            f"component_{idx}={comp['name']} "
            f"range={comp['start']}-{comp['end']} bytes={len(piece)} "
            f"sha256={piece_sha} manifest_sha256={comp['sha256']} "
            f"{'PASS' if ok else 'FAIL'}"
        )
    results["f"] = component_all
    print(f"check_f={'PASS' if component_all else 'FAIL'}")

    all_pass = all(results[key] for key in ("a", "b", "c", "d", "e", "f"))
    print(f"VERDICT: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
