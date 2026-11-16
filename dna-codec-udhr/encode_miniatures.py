#!/usr/bin/env python3
"""MINIATURES ENCODER — UDHR DNA lane (2026-11-15).
Two formula miniatures, encoded with the same house codec (UTF-8 bytes ->
bits MSB-first -> 00=A 01=C 10=G 11=T) and recorded alongside the UDHR
deposit. Each string is BUILT from explicit codepoints — never typed as a
glyph — because two of its characters have look-alikes: the typed glyph ℏ
is U+210F, but the specified character is U+0127; and Ĥ has a precomposed
form U+0124, but the specified form is H + a combining accent.

1. E=mc² — the squared sign is U+00B2 (SUPERSCRIPT TWO).
2. The Schrödinger equation in the exact form:  iℏ ∂Ψ/∂t = ĤΨ
   i = U+0069, ℏ = U+0127 (LATIN SMALL LETTER H WITH STROKE),
   ∂ = U+2202 (PARTIAL DIFFERENTIAL), Ψ = U+03A8 (GREEK CAPITAL LETTER PSI),
   Ĥ is NOT a single precomposed character: it is the letter H (U+0048)
   followed by U+0302 (COMBINING CIRCUMFLEX ACCENT)."""
import hashlib, json, re
from pathlib import Path

LANE = Path.home() / "workspace/dna-udhr-2026-11-15"

EMC2_CPS = [0x45, 0x3D, 0x6D, 0x63, 0xB2]                       # E = m c ²
SCHRODINGER_CPS = [0x69, 0x127, 0x20, 0x2202, 0x3A8, 0x2F, 0x2202, 0x74,
                   0x20, 0x3D, 0x20, 0x48, 0x302, 0x3A8]        # i ℏ ∂Ψ/∂t = ĤΨ
EMC2 = "".join(chr(c) for c in EMC2_CPS)
SCHRODINGER = "".join(chr(c) for c in SCHRODINGER_CPS)
assert [ord(c) for c in EMC2] == EMC2_CPS
assert [ord(c) for c in SCHRODINGER] == SCHRODINGER_CPS
assert EMC2 == "E=mc²"          # typed literal agrees (² is unambiguous)
# NOTE: no typed-literal assert for SCHRODINGER — a typed ℏ is U+210F and a
# typed Ĥ is U+0124; the codepoint list above is the specification.

ENC = {"00": "A", "01": "C", "10": "G", "11": "T"}

def encode(data: bytes) -> str:
    table = []
    for byte in range(256):
        bits = f"{byte:08b}"
        table.append("".join(ENC[bits[i:i + 2]] for i in range(0, 8, 2)))
    return "".join(table[b] for b in data)

def longest_run(seq: str) -> int:
    return max(len(m.group(0)) for m in re.finditer(r"(.)\1*", seq))

items = [
    ("E=mc²", "emc2", EMC2,
     "Mass-energy equivalence. The squared sign is U+00B2."),
    ("Schrödinger equation", "schrodinger", SCHRODINGER,
     "Exact form: iℏ ∂Ψ/∂t = ĤΨ, with ℏ = U+0127 and "
     "Ĥ = U+0048 + U+0302 (combining circumflex)."),
]
out = {}
lines = []
for label, key, s, note in items:
    data = s.encode("utf-8")
    seq = encode(data)
    assert len(seq) == 4 * len(data)
    out[key] = {
        "label": label,
        "string": s,
        "codepoints": [f"U+{ord(c):04X}" for c in s],
        "utf8_bytes": len(data),
        "utf8_hex": data.hex(),
        "bases": len(seq),
        "sequence": seq,
        "sha256_source_bytes": hashlib.sha256(data).hexdigest(),
        "sha256_base_stream": hashlib.sha256(seq.encode("ascii")).hexdigest(),
        "longest_homopolymer_run": longest_run(seq),
        "note": note,
    }
    lines.append(f"{key}: {seq}")
    print(json.dumps(out[key], indent=2, ensure_ascii=False))

(LANE / "miniatures-dna.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
(LANE / "work").mkdir(exist_ok=True)
(LANE / "work/miniatures.json").write_text(
    json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
print("miniatures written: miniatures-dna.txt, work/miniatures.json")
