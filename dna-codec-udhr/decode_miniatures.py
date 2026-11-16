#!/usr/bin/env python3
"""
Independent decoder for the two formula miniatures of the UDHR DNA lane.
Written from the written specification alone (2026-11-15).

Spec:
- miniatures-dna.txt holds one line per miniature: "key: SEQUENCE".
- Each base is two bits: A=00, C=01, G=10, T=11; four bases make one byte,
  most significant pair first.
- The decoded byte streams must equal, byte for byte, the UTF-8 encodings
  of the two specified strings, which this script rebuilds from their
  specified codepoints:
  * E=mc² — U+0045 U+003D U+006D U+0063 U+00B2.
  * iℏ ∂Ψ/∂t = ĤΨ — U+0069 U+0127 U+0020 U+2202 U+03A8 U+002F U+2202
    U+0074 U+0020 U+003D U+0020 U+0048 U+0302 U+03A8, where ℏ is U+0127
    (not the look-alike U+210F) and Ĥ is U+0048 followed by U+0302
    (not the precomposed U+0124).
"""
import hashlib
import os
import sys

SEQ_PATH = os.path.expanduser("~/workspace/dna-udhr-2026-11-15/miniatures-dna.txt")

BASE_TO_BITS = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}

EXPECTED = {
    "emc2": [0x45, 0x3D, 0x6D, 0x63, 0xB2],
    "schrodinger": [0x69, 0x127, 0x20, 0x2202, 0x3A8, 0x2F, 0x2202, 0x74,
                    0x20, 0x3D, 0x20, 0x48, 0x302, 0x3A8],
}


def decode_bases(base_str):
    if len(base_str) % 4 != 0:
        raise ValueError(f"Base count {len(base_str)} not divisible by 4")
    out = bytearray()
    for i in range(0, len(base_str), 4):
        b = 0
        for j, ch in enumerate(base_str[i:i+4]):
            b |= (BASE_TO_BITS[ch] << ((3 - j) * 2))
        out.append(b)
    return bytes(out)


def main():
    seqs = {}
    with open(SEQ_PATH, 'r', encoding='ascii') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            key, seq = line.split(": ", 1)
            seqs[key] = seq
    print(f"Sequence file: {SEQ_PATH}")
    print(f"Miniatures found: {sorted(seqs)}")

    all_pass = True
    for key, cps in EXPECTED.items():
        expected_str = "".join(chr(c) for c in cps)
        expected_bytes = expected_str.encode('utf-8')
        seq = seqs.get(key)
        if seq is None:
            print(f"{key}: MISSING — FAIL")
            all_pass = False
            continue
        decoded = decode_bases(seq)
        ok_bytes = decoded == expected_bytes
        ok_text = decoded.decode('utf-8') == expected_str
        ok_cps = [ord(c) for c in decoded.decode('utf-8')] == cps
        sha_src = hashlib.sha256(decoded).hexdigest()
        sha_base = hashlib.sha256(seq.encode('ascii')).hexdigest()
        print(f"{key}: bases={len(seq)} decoded_bytes={len(decoded)} "
              f"byte_identical={ok_bytes} text_equal={ok_text} "
              f"codepoints_equal={ok_cps}")
        print(f"  decoded: {decoded.decode('utf-8')!r}")
        print(f"  codepoints: {[f'U+{c:04X}' for c in cps]}")
        print(f"  SHA-256 decoded bytes: {sha_src}")
        print(f"  SHA-256 base stream: {sha_base}")
        ok = ok_bytes and ok_text and ok_cps
        print(f"  {'PASS' if ok else 'FAIL'}")
        all_pass = all_pass and ok

    print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
