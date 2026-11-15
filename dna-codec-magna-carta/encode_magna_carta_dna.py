#!/usr/bin/env python3
"""ENCODER — Magna Carta DNA lane (2026-11-14).
Encodes the 1215 Magna Carta in its original Latin EXACTLY as it stands
in the lane's source file, byte for byte, with the house codec (UTF-8
bytes -> bits MSB-first -> 00=A 01=C 10=G 11=T). The source file holds
the preamble and the 63 numbered clauses of the Bémont transcription of
the Cotton MS Augustus II.106 exemplar (Cii), with Holt's bracketed
cross-reference notes and footnote markers removed (see the manifest).
The encoder parses preamble + clauses to record per-clause byte and
base ranges. Aborts on any mismatch."""
import hashlib, json, re, sys
from pathlib import Path

LANE = Path.home() / "workspace/dna-magna-carta-2026-11-14"
SOURCE = LANE / "magna-carta-1215-latin-source.txt"

raw = SOURCE.read_bytes()
sha = hashlib.sha256(raw).hexdigest()
text = raw.decode("utf-8")
if not all(ord(ch) < 128 for ch in text):
    sys.exit("ABORT: source is not pure ASCII as expected for this transcription")

# ---- structure parse: preamble paragraph + 63 numbered clause paragraphs ----
paragraphs = text.rstrip("\n").split("\n\n")
if len(paragraphs) != 64:
    sys.exit(f"ABORT: found {len(paragraphs)} paragraphs, expected 64 (preamble + 63 clauses)")
if not paragraphs[0].startswith("Johannes dei gracia rex Anglie"):
    sys.exit("ABORT: preamble does not open with 'Johannes dei gracia rex Anglie'")

CLAUSE_RE = re.compile(r"^(\d+)\.")
segments = [{"label": "Preamble", "kind": "preamble", "clause": 0,
             "byte_start": 0, "byte_end": len(paragraphs[0].encode("utf-8")),
             "text_bytes": len(paragraphs[0].encode("utf-8")),
             "base_start": 1, "base_end": len(paragraphs[0].encode("utf-8")) * 4}]
pos = len(paragraphs[0].encode("utf-8")) + 2
for i, p in enumerate(paragraphs[1:], 1):
    m = CLAUSE_RE.match(p)
    if not m:
        sys.exit(f"ABORT: paragraph {i + 1} does not open with a clause number")
    n = int(m.group(1))
    if n != i:
        sys.exit(f"ABORT: clause sequence broken at paragraph {i + 1}: found {n}, expected {i}")
    b = len(p.encode("utf-8"))
    segments.append({"label": f"Clause {n}", "kind": "clause", "clause": n,
                     "byte_start": pos, "byte_end": pos + b, "text_bytes": b,
                     "base_start": pos * 4 + 1, "base_end": (pos + b) * 4})
    pos += b + 2
assert pos - 2 + 1 == len(raw), (pos, len(raw))  # last clause + trailing '\n'

# Extend each segment's span to the next segment's first byte (the last
# to end-of-file), so the spans tile the stream exactly: the blank-line
# separator after each paragraph is carried inside that paragraph's
# span, and the file's final newline inside clause 63's span.
for i, s in enumerate(segments):
    end = segments[i + 1]["byte_start"] if i + 1 < len(segments) else len(raw)
    s["byte_end"] = end
    s["base_end"] = end * 4
cursor = 0
for s in segments:
    assert s["byte_start"] == cursor, (s, cursor)
    cursor = s["byte_end"]
assert cursor == len(raw)
if not paragraphs[-1].endswith("anno regni nostri decimo septimo."):
    sys.exit("ABORT: clause 63 does not close with 'anno regni nostri decimo septimo.'")

# ---- encode ----
ENC = {"00": "A", "01": "C", "10": "G", "11": "T"}
table = []
for byte in range(256):
    bits = f"{byte:08b}"
    table.append("".join(ENC[bits[i:i + 2]] for i in range(0, 8, 2)))
bases = "".join(table[b] for b in raw)
assert len(bases) == 4 * len(raw)

seq_path = LANE / "magna-carta-dna.txt"
with seq_path.open("w", encoding="ascii") as f:
    for i in range(0, len(bases), 60):
        f.write(bases[i:i + 60] + "\n")

sha_bases = hashlib.sha256(bases.encode("ascii")).hexdigest()
fig = {"source_file": str(SOURCE), "source_bytes": len(raw), "source_sha256": sha,
       "total_bases": len(bases), "sha256_base_stream": sha_bases,
       "segments": segments}
(LANE / "work").mkdir(exist_ok=True)
(LANE / "work/encoder.json").write_text(json.dumps(fig, indent=1), encoding="utf-8")
print(json.dumps({"source_bytes": len(raw), "source_sha256": sha,
                  "total_bases": len(bases), "sha256_base_stream": sha_bases,
                  "clauses": 63,
                  "sequence_file_bytes": seq_path.stat().st_size}, indent=2))
