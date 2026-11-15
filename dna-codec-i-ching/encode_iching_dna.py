#!/usr/bin/env python3
"""ENCODER — I Ching DNA lane (2026-11-14).
Encodes Robert Tilford's I Ching draft AS IT STANDS with the house codec
(UTF-8 bytes -> bits MSB-first -> 00=A 01=C 10=G 11=T).

THE DRAFT AS IT STANDS: no single assembled master file exists on disk.
The draft of record is seven files in ~/workspace/iching/ — the pilot
(Hexagrams 1–2) and six post-pilot batches (Hexagrams 3–50) — totalling
352 of 450 units drafted, 240 of 450 approved. This encoder assembles
the lane's source of record by PURE CONCATENATION of those seven files'
bytes in drafting order: nothing added, nothing removed, nothing
altered. Each component file's size and SHA-256 are verified before
assembly and recorded, with its byte range in the assembly, so any
reader can split the decoded stream back into the exact seven files.
Aborts on any mismatch."""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path.home() / "workspace"
LANE = ROOT / "dna-iching-2026-11-14"
SRC_DIR = ROOT / "iching"

# (filename, hexagrams, units, status) — drafting order
COMPONENTS = [
    ("PILOT-HEXAGRAMS-01-02-DRAFT-2026-11-08.md", "1–2", 16,
     "APPROVED (2026-11-09)",
     12894, "eb009c4a7b35c58f69005119e38ae8665510f6f062d692bd2b9cd8157f5b2033"),
    ("WAVE-4-DRAFT-HEXAGRAMS-03-10-DRAFT-2026-11-09.md", "3–10", 56,
     "APPROVED (2026-11-09)",
     33605, "90438a63f4052f708edd2e5242124c7c6f6f2df965547f90269f9dbeedf227ab"),
    ("WAVE-4-DRAFT-HEXAGRAMS-11-18-DRAFT-2026-11-09.md", "11–18", 56,
     "APPROVED (2026-11-09)",
     38835, "2f114612a600786e9894923be1ea0988cdf08e3abc360b6ba788f88e44f7842f"),
    ("WAVE-4-DRAFT-HEXAGRAMS-19-26-DRAFT-2026-11-09.md", "19–26", 56,
     "APPROVED (2026-11-09)",
     40791, "0564efb41e99b593c384254398fc31fd4fe125bc64af24ac9bcb722920263527"),
    ("WAVE-4-DRAFT-HEXAGRAMS-27-34-DRAFT-2026-11-09.md", "27–34", 56,
     "APPROVED (2026-11-09)",
     42719, "8c15b0ce695fb6e857dc60decfa0dc7c5578d95c508c2640ee1c978e3a95f849"),
    ("WAVE-4-DRAFT-HEXAGRAMS-35-42-DRAFT-2026-11-09.md", "35–42", 56,
     "DRAFTED, desk-graded 2026-11-09, awaiting Robert's read",
     46395, "5fbd6dea06594330c697cb10a5841f8dcf41ac228e03d0649bdc5fb2dac30e3e"),
    ("WAVE-5-DRAFT-HEXAGRAMS-43-50-DRAFT-2026-11-11.md", "43–50", 56,
     "DRAFTED ONLY — not graded, not read, not approved",
     60952, "eb8283e6e902e63efd7a92b038bb8e33dd7b8e59e7dc0faf26f23db4158cbb85"),
]

parts = []
components = []
cursor = 0
for fn, hexes, units, status, exp_bytes, exp_sha in COMPONENTS:
    data = (SRC_DIR / fn).read_bytes()
    if len(data) != exp_bytes:
        sys.exit(f"ABORT: {fn} is {len(data)} bytes, expected {exp_bytes}")
    h = hashlib.sha256(data).hexdigest()
    if h != exp_sha:
        sys.exit(f"ABORT: {fn} SHA-256 {h} != expected {exp_sha}")
    components.append({"file": fn, "hexagrams": hexes, "units": units,
                       "status": status, "bytes": len(data), "sha256": h,
                       "byte_start": cursor, "byte_end": cursor + len(data),
                       "base_start": cursor * 4 + 1,
                       "base_end": (cursor + len(data)) * 4})
    parts.append(data)
    cursor += len(data)

raw = b"".join(parts)
assert len(raw) == cursor == 276191, len(raw)
sha = hashlib.sha256(raw).hexdigest()

ASSEMBLY = LANE / "I-CHING-DRAFT-ASSEMBLY-352-OF-450.txt"
ASSEMBLY.write_bytes(raw)
assert ASSEMBLY.read_bytes() == raw

# ---- structure parse over the assembly (line-based byte offsets) ----
text = raw.decode("utf-8")
lines = text.split("\n")
offsets = []
pos = 0
for l in lines:
    offsets.append(pos)
    pos += len(l.encode("utf-8")) + 1
assert pos - 1 == len(raw) or (pos == len(raw) + 1 and lines[-1] == "")

HEX_RE = re.compile(r"^## HEXAGRAM (\d+) — (.+)$")
hex_lines = []
for i, l in enumerate(lines):
    m = HEX_RE.match(l)
    if m:
        hex_lines.append((i, int(m.group(1)), m.group(2).strip()))
if len(hex_lines) != 50:
    sys.exit(f"ABORT: found {len(hex_lines)} hexagram headings, expected 50")
if [n for _, n, _ in hex_lines] != list(range(1, 51)):
    sys.exit("ABORT: hexagram numbers not sequential 1..50")

def file_end_for(byte_pos):
    for c in components:
        if c["byte_start"] <= byte_pos < c["byte_end"]:
            return c["byte_end"]
    return len(raw)

hexagrams = []
for k, (li, n, title) in enumerate(hex_lines):
    s = offsets[li]
    next_head = offsets[hex_lines[k + 1][0]] if k + 1 < len(hex_lines) else len(raw)
    e = min(next_head, file_end_for(s))
    hexagrams.append({"hexagram": n, "title": title, "byte_start": s, "byte_end": e,
                      "base_start": s * 4 + 1, "base_end": e * 4})

segments = [{"label": f"{c['file']} (Hexagrams {c['hexagrams']})", "kind": "component",
             "byte_start": c["byte_start"], "byte_end": c["byte_end"],
             "base_start": c["base_start"], "base_end": c["base_end"]}
            for c in components]
cur = 0
for s in segments:
    assert s["byte_start"] == cur, f"gap/overlap before {s['label']}"
    cur = s["byte_end"]
assert cur == len(raw)

# ---- encode ----
ENC = {"00": "A", "01": "C", "10": "G", "11": "T"}
table = []
for byte in range(256):
    bits = f"{byte:08b}"
    table.append("".join(ENC[bits[i:i + 2]] for i in range(0, 8, 2)))
bases = "".join(table[b] for b in raw)
assert len(bases) == 4 * len(raw)

seq_path = LANE / "iching-dna-full.txt"
with seq_path.open("w", encoding="ascii") as f:
    for i in range(0, len(bases), 60):
        f.write(bases[i:i + 60] + "\n")

sha_bases = hashlib.sha256(bases.encode("ascii")).hexdigest()
fig = {"source_file": str(ASSEMBLY), "assembly_method":
       "pure concatenation of the seven component files' bytes in drafting "
       "order; nothing added, removed, or altered",
       "components": components, "source_bytes": len(raw), "source_sha256": sha,
       "total_bases": len(bases), "sha256_base_stream": sha_bases,
       "hexagrams": hexagrams, "segments": segments,
       "units_drafted": 352, "units_total": 450, "units_approved": 240}
(LANE / "work").mkdir(exist_ok=True)
(LANE / "work/encoder.json").write_text(json.dumps(fig, indent=1), encoding="utf-8")
print(json.dumps({"assembly_bytes": len(raw), "assembly_sha256": sha,
                  "total_bases": len(bases), "sha256_base_stream": sha_bases,
                  "components": len(components), "hexagrams": len(hexagrams),
                  "sequence_file_bytes": seq_path.stat().st_size}, indent=2))
