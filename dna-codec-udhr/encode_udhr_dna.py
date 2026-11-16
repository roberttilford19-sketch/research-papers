#!/usr/bin/env python3
"""ENCODER — UDHR DNA lane (2026-11-15).
Encodes the lane's source of record (the Universal Declaration of Human
Rights as published by the United Nations, constructed by build_source.py)
EXACTLY as it stands, byte for byte, with the house codec (UTF-8 bytes ->
bits MSB-first -> 00=A 01=C 10=G 11=T). Also parses the source's own
structure (title, Preamble with its ten paragraphs, Articles 1-30) to record
per-section byte and base ranges. Aborts on any mismatch."""
import hashlib, json, re, sys
from pathlib import Path

LANE = Path.home() / "workspace/dna-udhr-2026-11-15"
SOURCE = LANE / "udhr-un-official-text.txt"
EXPECTED_BYTES = 10821
EXPECTED_SHA256 = "bfd143dd10de856ef2c86becc2a97155d21810389813cef8c530e05b8ab085db"

raw = SOURCE.read_bytes()
if len(raw) != EXPECTED_BYTES:
    sys.exit(f"ABORT: source is {len(raw)} bytes, expected {EXPECTED_BYTES}")
sha = hashlib.sha256(raw).hexdigest()
if sha != EXPECTED_SHA256:
    sys.exit(f"ABORT: source SHA-256 {sha} != expected {EXPECTED_SHA256}")
text = raw.decode("utf-8")

# ---- structure parse (blank-line blocks; byte offsets accumulated) ----
blocks = text[:-1].split("\n\n") if text.endswith("\n") else text.split("\n\n")
offsets = []
pos = 0
for b in blocks:
    offsets.append(pos)
    pos += len(b.encode("utf-8")) + 2  # +2 for the '\n\n' separator
assert pos - 2 + 1 == len(raw), f"block tiling off: {pos} vs {len(raw)}"

ART_RE = re.compile(r"^Article (\d+)$")
segments = []   # (label, kind, byte_start, byte_end)
articles = []   # per-article records
i = 0
if blocks[0] != "Universal Declaration of Human Rights":
    sys.exit("ABORT: first block is not the title")
segments.append(("Title", "title", offsets[0], offsets[1] - 2))
i = 1
if blocks[i] != "Preamble":
    sys.exit("ABORT: second block is not the Preamble heading")
pre_start = offsets[i]
i += 1
n_pre = 0
while i < len(blocks) and not ART_RE.match(blocks[i]):
    n_pre += 1
    i += 1
if n_pre != 10:
    sys.exit(f"ABORT: preamble has {n_pre} paragraphs, expected 10")
segments.append(("Preamble", "preamble", pre_start, offsets[i] - 2))
while i < len(blocks):
    m = ART_RE.match(blocks[i])
    if not m:
        sys.exit(f"ABORT: expected an Article heading at block {i}, got {blocks[i][:40]!r}")
    n = int(m.group(1))
    start = offsets[i]
    i += 1
    n_par = 0
    while i < len(blocks) and not ART_RE.match(blocks[i]):
        n_par += 1
        i += 1
    end = (offsets[i] - 2) if i < len(blocks) else len(raw) - 1
    articles.append({"article": n, "paragraphs": n_par,
                     "byte_start": start, "byte_end": end,
                     "base_start": start * 4 + 1, "base_end": end * 4})
    segments.append((f"Article {n}", "article", start, end))
nums = [a["article"] for a in articles]
if nums != list(range(1, 31)):
    sys.exit(f"ABORT: article numbers not sequential 1..30: {nums}")

# Segments tile the block region: each segment after the first begins
# exactly one blank-line separator (2 bytes) after the previous segment ends;
# the file's single trailing newline stands after the last segment.
cursor = 0
for label, kind, s, e in segments:
    assert s == cursor, f"gap/overlap before segment {label}: {s} != {cursor}"
    cursor = e + 2
assert cursor - 2 == len(raw) - 1, \
    f"segments end at {cursor - 2}, file body is {len(raw) - 1}"

# ---- encode ----
ENC = {"00": "A", "01": "C", "10": "G", "11": "T"}
table = []
for byte in range(256):
    bits = f"{byte:08b}"
    table.append("".join(ENC[bits[i:i + 2]] for i in range(0, 8, 2)))
bases = "".join(table[b] for b in raw)
assert len(bases) == 4 * len(raw)

seq_path = LANE / "udhr-dna-full.txt"
with seq_path.open("w", encoding="ascii") as f:
    for j in range(0, len(bases), 60):
        f.write(bases[j:j + 60] + "\n")

sha_bases = hashlib.sha256(bases.encode("ascii")).hexdigest()
fig = {"source_file": str(SOURCE), "source_bytes": len(raw), "source_sha256": sha,
       "total_bases": len(bases), "sha256_base_stream": sha_bases,
       "articles": articles,
       "segments": [{"label": l, "kind": k, "byte_start": s, "byte_end": e,
                     "base_start": s * 4 + 1, "base_end": e * 4}
                    for l, k, s, e in segments]}
(LANE / "work").mkdir(exist_ok=True)
(LANE / "work/encoder.json").write_text(json.dumps(fig, indent=1), encoding="utf-8")
print(json.dumps({"source_bytes": len(raw), "source_sha256": sha,
                  "total_bases": len(bases), "sha256_base_stream": sha_bases,
                  "articles": len(articles),
                  "sequence_file_bytes": seq_path.stat().st_size}, indent=2))
