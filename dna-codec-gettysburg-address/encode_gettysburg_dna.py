#!/usr/bin/env python3
"""ENCODER — Gettysburg Address DNA lane (2026-11-14).
Encodes the Bliss copy of the Gettysburg Address EXACTLY as it stands in
the lane's source file, byte for byte, with the house codec (UTF-8 bytes
-> bits MSB-first -> 00=A 01=C 10=G 11=T). The source file holds the three
paragraphs of the Address as printed in the Library of Congress
exhibition text of the Bliss copy. The encoder parses the three
paragraphs to record per-paragraph byte and base ranges. Aborts on any
mismatch."""
import hashlib, json, sys
from pathlib import Path

LANE = Path.home() / "workspace/dna-gettysburg-2026-11-14"
SOURCE = LANE / "gettysburg-address-source.txt"

raw = SOURCE.read_bytes()
sha = hashlib.sha256(raw).hexdigest()
text = raw.decode("utf-8")

# ---- structure parse: three paragraphs separated by blank lines ----
paragraphs = text.rstrip("\n").split("\n\n")
if len(paragraphs) != 3:
    sys.exit(f"ABORT: found {len(paragraphs)} paragraphs, expected 3")
if not paragraphs[0].startswith("Four score and seven years ago"):
    sys.exit("ABORT: paragraph 1 does not open with 'Four score and seven years ago'")
if not paragraphs[2].endswith("shall not perish from the earth."):
    sys.exit("ABORT: paragraph 3 does not close with 'shall not perish from the earth.'")

segments = []
pos = 0
for i, p in enumerate(paragraphs, 1):
    b = len(p.encode("utf-8"))
    segments.append({"label": f"Paragraph {i}", "kind": "paragraph",
                     "byte_start": pos, "byte_end": pos + b, "text_bytes": b,
                     "base_start": pos * 4 + 1, "base_end": (pos + b) * 4})
    pos += b + 2  # +2 for the blank-line separator '\n\n'
assert pos - 2 + 1 == len(raw), (pos, len(raw))  # last paragraph + trailing '\n'

# Extend each segment's span to the next segment's first byte (the last
# to end-of-file), so the spans tile the stream exactly: the blank-line
# separator after each paragraph is carried inside that paragraph's
# span, and the file's final newline inside the last paragraph's span.
for i, s in enumerate(segments):
    end = segments[i + 1]["byte_start"] if i + 1 < len(segments) else len(raw)
    s["byte_end"] = end
    s["base_end"] = end * 4
cursor = 0
for s in segments:
    assert s["byte_start"] == cursor, (s, cursor)
    cursor = s["byte_end"]
assert cursor == len(raw)

# ---- encode ----
ENC = {"00": "A", "01": "C", "10": "G", "11": "T"}
table = []
for byte in range(256):
    bits = f"{byte:08b}"
    table.append("".join(ENC[bits[i:i + 2]] for i in range(0, 8, 2)))
bases = "".join(table[b] for b in raw)
assert len(bases) == 4 * len(raw)

seq_path = LANE / "gettysburg-dna.txt"
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
                  "paragraphs": len(segments),
                  "sequence_file_bytes": seq_path.stat().st_size}, indent=2))
