#!/usr/bin/env python3
"""ENCODER — Tao Te Ching DNA lane (2026-11-14).
Encodes Robert Tilford's Tao Te Ching translation master EXACTLY as it
stands, byte for byte, with the house codec (UTF-8 bytes -> bits MSB-first
-> 00=A 01=C 10=G 11=T). No extraction, no retyping: the source file's raw
bytes are the stream. Also parses the source's own structure (81 chapter
headings under two part headings) to record per-chapter byte and base
ranges for the printed book's index. Aborts on any mismatch."""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path.home() / "workspace"
LANE = ROOT / "dna-tao-2026-11-14"
SOURCE = ROOT / "your_files/TAO-TE-CHING-THE-TILFORD-TRANSLATION-DRAFT-2026-10-31.md"
EXPECTED_BYTES = 75787
EXPECTED_SHA256 = "2a73e08bd0599e0de6f30e9f68b0dcbb3746ccd1b2a0c56937336c8741a111f1"

raw = SOURCE.read_bytes()
if len(raw) != EXPECTED_BYTES:
    sys.exit(f"ABORT: source is {len(raw)} bytes, expected {EXPECTED_BYTES}")
sha = hashlib.sha256(raw).hexdigest()
if sha != EXPECTED_SHA256:
    sys.exit(f"ABORT: source SHA-256 {sha} != expected {EXPECTED_SHA256}")
text = raw.decode("utf-8")

# ---- structure parse (line-based; byte offsets accumulated incrementally) ----
lines = text.split("\n")
offsets = []
pos = 0
for l in lines:
    offsets.append(pos)
    pos += len(l.encode("utf-8")) + 1  # +1 for the '\n'
assert pos - 1 == len(raw) or (pos == len(raw) + 1 and lines[-1] == "")

CHAP_RE = re.compile(r"^## .+ · Chapter (\d+)\s*$")
PART_RE = re.compile(r"^# .+ — The Book of (?:the )?(Way|Virtue) \(Chapters (\d+)–(\d+)\)\s*$")

part_lines = []   # (line_idx, part_no, title, first_ch, last_ch)
chap_lines = []   # (line_idx, chapter_no)
for i, l in enumerate(lines):
    m = PART_RE.match(l)
    if m:
        part_lines.append((i, len(part_lines) + 1, l.lstrip("# ").strip(),
                           int(m.group(2)), int(m.group(3))))
        continue
    m = CHAP_RE.match(l)
    if m:
        chap_lines.append((i, int(m.group(1))))

if len(part_lines) != 2:
    sys.exit(f"ABORT: found {len(part_lines)} part headings, expected 2")
if len(chap_lines) != 81:
    sys.exit(f"ABORT: found {len(chap_lines)} chapter headings, expected 81")
nums = [n for _, n in chap_lines]
if nums != list(range(1, 82)):
    sys.exit(f"ABORT: chapter numbers not sequential 1..81: {nums[:10]}...")
for (li, pno, title, fc, lc) in part_lines:
    inside = [n for (ci, n) in chap_lines if ci > li]
    expect = list(range(fc, lc + 1))
    got = [n for n in inside if n in expect]
    if got != expect:
        sys.exit(f"ABORT: part {pno} chapters {got[:5]}... != declared {fc}-{lc}")

def byte_span(start_line, end_line_exclusive):
    s = offsets[start_line]
    e = offsets[end_line_exclusive] if end_line_exclusive < len(lines) else len(raw)
    return s, e

segments = []   # (label, kind, byte_start, byte_end)
chapters = []   # per-chapter records
segments.append(("Front matter of the edition", "front",
                 0, offsets[part_lines[0][0]]))
for pi, (li, pno, title, fc, lc) in enumerate(part_lines):
    next_part_line = part_lines[pi + 1][0] if pi + 1 < len(part_lines) else len(lines)
    first_ch_line = next(ci for ci, n in chap_lines if n == fc)
    hs, he = byte_span(li, first_ch_line)
    segments.append((title, "part", hs, he))
    for ci, n in [(c, nn) for c, nn in chap_lines if fc <= nn <= lc]:
        nxt_ch = next((c2 for c2, n2 in chap_lines if n2 == n + 1), len(lines))
        end_line = min(nxt_ch, next_part_line)
        cs, ce = byte_span(ci, end_line)
        chapters.append({"chapter": n, "part": pno, "byte_start": cs, "byte_end": ce,
                         "base_start": cs * 4 + 1, "base_end": ce * 4})
        segments.append((f"Chapter {n}", "chapter", cs, ce))
parts = [{"part": pno, "title": title, "first_chapter": fc, "last_chapter": lc,
          "byte_start": [c for c in chapters if c["chapter"] == fc][0]["byte_start"],
          "byte_end": [c for c in chapters if c["chapter"] == lc][0]["byte_end"]}
         for (li, pno, title, fc, lc) in part_lines]
for p in parts:
    p["base_start"] = p["byte_start"] * 4 + 1
    p["base_end"] = p["byte_end"] * 4
# fold the part-heading segments into the parts' byte spans for the index:
# (part byte_start above begins at its first chapter; the heading segment is separate)

# segments must tile the file exactly
cursor = 0
for label, kind, s, e in segments:
    assert s == cursor, f"gap/overlap before segment {label}: {s} != {cursor}"
    cursor = e
assert cursor == len(raw), f"segments end at {cursor}, file is {len(raw)}"

# ---- encode ----
ENC = {"00": "A", "01": "C", "10": "G", "11": "T"}
table = []
for byte in range(256):
    bits = f"{byte:08b}"
    table.append("".join(ENC[bits[i:i + 2]] for i in range(0, 8, 2)))
bases = "".join(table[b] for b in raw)
assert len(bases) == 4 * len(raw)

seq_path = LANE / "tao-dna-full.txt"
with seq_path.open("w", encoding="ascii") as f:
    for i in range(0, len(bases), 60):
        f.write(bases[i:i + 60] + "\n")

sha_bases = hashlib.sha256(bases.encode("ascii")).hexdigest()
fig = {"source_file": str(SOURCE), "source_bytes": len(raw), "source_sha256": sha,
       "total_bases": len(bases), "sha256_base_stream": sha_bases,
       "parts": parts, "chapters": chapters,
       "segments": [{"label": l, "kind": k, "byte_start": s, "byte_end": e,
                     "base_start": s * 4 + 1, "base_end": e * 4}
                    for l, k, s, e in segments]}
(LANE / "work").mkdir(exist_ok=True)
(LANE / "work/encoder.json").write_text(json.dumps(fig, indent=1), encoding="utf-8")
print(json.dumps({"source_bytes": len(raw), "source_sha256": sha,
                  "total_bases": len(bases), "sha256_base_stream": sha_bases,
                  "chapters": len(chapters), "parts": len(parts),
                  "sequence_file_bytes": seq_path.stat().st_size}, indent=2))
