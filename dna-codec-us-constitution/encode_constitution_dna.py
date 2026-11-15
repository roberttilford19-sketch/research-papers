#!/usr/bin/env python3
"""ENCODER — U.S. Constitution DNA lane (2026-11-14).
Encodes the lane's source of record EXACTLY as it stands, byte for byte,
with the house codec (UTF-8 bytes -> bits MSB-first -> 00=A 01=C 10=G
11=T). The source of record (us-constitution-nara-transcription.txt)
was constructed by build_source.py from the National Archives
founding-docs transcriptions; see that script and the manifest for the
exact source and the exact extraction rule.

This encoder parses the source's structure and PROVES completeness as
it parses: the Preamble; Articles I-VII in order with their section
counts (10/4/3/4/0/0/0); the attestation and signature blocks (12 state
headings, 39 signers, ending with Gouv Morris); Amendments 1-27 in
order with their section counts; no editorial apparatus anywhere (no
"Note:" annotations, no "Passed by Congress" date lines). It also runs
phrase-level spot cross-checks against Project Gutenberg eBook #5 (a
different edition of the 1787 text; used only as a cross-check — that
eBook itself states it does not include the amendments). Segments must
tile the file exactly. Aborts on any mismatch."""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path.home() / "workspace"
LANE = ROOT / "dna-constitution-2026-11-14"
SOURCE = LANE / "us-constitution-nara-transcription.txt"
PG5 = LANE / "source/constitution-gutenberg-candidate.txt"

raw = SOURCE.read_bytes()
sha = hashlib.sha256(raw).hexdigest()
text = raw.decode("utf-8")
if not text.endswith("\n") or text.endswith("\n\n"):
    sys.exit("ABORT: source must end with exactly one newline")
blocks = text[:-1].split("\n\n")

# ---- tiling: locate each block in the raw bytes, gaps exactly "\n\n" ----
offsets = []
pos = 0
for b in blocks:
    i = text.find(b, pos)
    assert i == pos, f"block not at expected offset {pos}: {b[:50]!r}"
    offsets.append(pos)
    pos += len(b) + 2
assert pos - 2 + 1 == len(text)  # last block + trailing newline

def boff(char_off):
    return len(text[:char_off].encode("utf-8"))

ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
         "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13,
         "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18,
         "XIX": 19, "XX": 20, "XXI": 21, "XXII": 22, "XXIII": 23,
         "XXIV": 24, "XXV": 25, "XXVI": 26, "XXVII": 27}
ART_RE = re.compile(r"^Article\. ([IVX]+)\.$")
AMD_RE = re.compile(r"^(?:Amendment|AMENDMENT) ([IVX]+)$")
SEC_RE = re.compile(r"^Section\.? (\d+)\.$")

def is_heading(b):
    return bool(ART_RE.match(b) or AMD_RE.match(b) or SEC_RE.match(b))

# ---- structural parse ----
segments = []   # (label, kind, first_block, last_block_exclusive)
units = []      # articles/amendments with section counts

if not blocks[0].startswith("We the People of the United States, in Order to form"):
    sys.exit("ABORT: first block is not the Preamble")
if "do ordain and establish this Constitution for the United States of America." not in blocks[0]:
    sys.exit("ABORT: Preamble closing words missing")
segments.append(("Preamble", "preamble", 0, 1))

EXPECTED_ARTICLE_SECTIONS = {1: 10, 2: 4, 3: 3, 4: 4, 5: 0, 6: 0, 7: 0}
EXPECTED_AMENDMENT_SECTIONS = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
                               8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 2,
                               14: 5, 15: 2, 16: 0, 17: 0, 18: 3, 19: 0,
                               20: 6, 21: 3, 22: 2, 23: 2, 24: 2, 25: 4,
                               26: 2, 27: 0}
STATES = ["Delaware", "Maryland", "Virginia", "North Carolina",
          "South Carolina", "Georgia", "New Hampshire", "Massachusetts",
          "Connecticut", "New York", "New Jersey", "Pennsylvania"]

idx = 1
for art in range(1, 8):
    if idx >= len(blocks):
        sys.exit(f"ABORT: ran out of blocks at Article {art}")
    m = ART_RE.match(blocks[idx])
    if not m or ROMAN[m.group(1)] != art:
        sys.exit(f"ABORT: expected Article {art} heading, found {blocks[idx][:40]!r}")
    start = idx
    idx += 1
    secs = []
    while idx < len(blocks) and not ART_RE.match(blocks[idx]) and not AMD_RE.match(blocks[idx]):
        sm = SEC_RE.match(blocks[idx])
        if sm:
            secs.append(int(sm.group(1)))
        idx += 1
    # Article VII is followed by the attestation material, which is not
    # part of the article segment; stop the article at its text end.
    if art == 7:
        # blocks: [heading, ratification paragraph] only
        end = start + 2
        if "The Ratification of the Conventions of nine States" not in blocks[start + 1]:
            sys.exit("ABORT: Article VII ratification text missing")
        segments.append((f"Article {art}", "article", start, end))
        units.append({"unit": f"Article {art}", "kind": "article",
                      "number": art, "sections": 0})
        idx = end
        break
    if secs != list(range(1, EXPECTED_ARTICLE_SECTIONS[art] + 1)):
        sys.exit(f"ABORT: Article {art} sections {secs} != 1..{EXPECTED_ARTICLE_SECTIONS[art]}")
    segments.append((f"Article {art}", "article", start, idx))
    units.append({"unit": f"Article {art}", "kind": "article",
                  "number": art, "sections": len(secs)})

# ---- attestation and signatures ----
start = idx
while idx < len(blocks) and not AMD_RE.match(blocks[idx]):
    idx += 1
att = blocks[start:idx]
att_text = "\n\n".join(att)
for needle in ("Attest William Jackson Secretary",
               "done in Convention by the Unanimous Consent of the States present",
               "G°. Washington", "Presidt and deputy from Virginia"):
    if needle not in att_text:
        sys.exit(f"ABORT: attestation segment missing {needle!r}")
state_heads = [b for b in att if b in STATES]
if state_heads != STATES:
    sys.exit(f"ABORT: state signature headings {state_heads} != {STATES}")
signer_lines = []
for j, b in enumerate(att):
    if b in STATES:
        signer_lines += att[j + 1].split("\n")
    elif b.startswith("G°. Washington"):
        signer_lines.append("G°. Washington")
if len(signer_lines) != 39:
    sys.exit(f"ABORT: counted {len(signer_lines)} signers, expected 39")
if att[-1].split("\n")[-1] != "Gouv Morris":
    sys.exit("ABORT: signature blocks do not end with Gouv Morris")
segments.append(("Attestation and signatures", "attestation", start, idx))

# ---- amendments 1-27 ----
for amd in range(1, 28):
    if idx >= len(blocks):
        sys.exit(f"ABORT: ran out of blocks at Amendment {amd}")
    m = AMD_RE.match(blocks[idx])
    if not m or ROMAN[m.group(1)] != amd:
        sys.exit(f"ABORT: expected Amendment {amd} heading, found {blocks[idx][:40]!r}")
    start = idx
    idx += 1
    secs = []
    while idx < len(blocks) and not AMD_RE.match(blocks[idx]):
        sm = SEC_RE.match(blocks[idx])
        if sm:
            secs.append(int(sm.group(1)))
        idx += 1
    if secs != list(range(1, EXPECTED_AMENDMENT_SECTIONS[amd] + 1)):
        sys.exit(f"ABORT: Amendment {amd} sections {secs} != "
                 f"1..{EXPECTED_AMENDMENT_SECTIONS[amd]}")
    segments.append((f"Amendment {amd}", "amendment", start, idx))
    units.append({"unit": f"Amendment {amd}", "kind": "amendment",
                  "number": amd, "sections": len(secs)})
if idx != len(blocks):
    sys.exit(f"ABORT: {len(blocks) - idx} blocks left over after Amendment 27")

# ---- no editorial apparatus anywhere ----
for b in blocks:
    if b.startswith("Note:") or "Passed by Congress" in b or "Ratified" in b.split("\n")[0] and b.startswith("Passed"):
        sys.exit(f"ABORT: editorial apparatus present: {b[:60]!r}")

# ---- key-phrase proofs ----
FULL = text
for needle in (
    "Congress shall make no law respecting an establishment of religion",
    "No law, varying the compensation for the services of the Senators and "
    "Representatives, shall take effect, until an election of Representatives "
    "shall have intervened.",
    "The Privilege of the Writ of Habeas Corpus shall not be suspended",
    "Neither slavery nor involuntary servitude, except as a punishment for crime",
):
    if needle not in FULL:
        sys.exit(f"ABORT: key phrase missing: {needle[:50]!r}")

# ---- phrase-level spot cross-checks vs Project Gutenberg eBook #5 ----
def norm(s):
    return re.sub(r"[^a-z0-9 ]+", " ", s.lower()).split()
pg_words = norm(PG5.read_text(encoding="utf-8"))
src_words = norm(text)
def phrase_in(words, phrase):
    pw = norm(phrase)
    n = len(pw)
    return any(words[i:i + n] == pw for i in range(len(words) - n + 1))
CROSS = [
    "The Ratification of the Conventions of nine States shall be sufficient for the Establishment of this Constitution",
    "No Title of Nobility shall be granted by the United States",
    "Treason against the United States shall consist only in levying War against them",
    "Full Faith and Credit shall be given in each State to the public Acts Records and judicial Proceedings of every other State",
    "The Congress shall have Power To lay and collect Taxes Duties Imposts and Excises",
    "All Bills for raising Revenue shall originate in the House of Representatives",
]
cross = []
for ph in CROSS:
    cross.append({"phrase": ph, "in_source": phrase_in(src_words, ph),
                  "in_gutenberg_5": phrase_in(pg_words, ph)})
    if not (cross[-1]["in_source"] and cross[-1]["in_gutenberg_5"]):
        sys.exit(f"ABORT: cross-check phrase failed: {ph[:60]!r} -> {cross[-1]}")

# ---- segment byte spans ----
seg_records = []
for label, kind, fb, lb in segments:
    cs = boff(offsets[fb])
    ce = boff(offsets[lb - 1] + len(blocks[lb - 1]))
    seg_records.append({"label": label, "kind": kind, "byte_start": cs,
                        "byte_end": ce, "base_start": cs * 4 + 1,
                        "base_end": ce * 4})
cursor = 0
for s in seg_records:
    # segments are separated by exactly one blank line ("\n\n"): a
    # segment begins 2 bytes after the previous segment's end, except
    # the first (0) — verify no gaps beyond the separators.
    assert s["byte_start"] in (cursor, cursor + 2), (s, cursor)
    cursor = s["byte_end"]
assert cursor == len(raw) - 1  # trailing single newline after last block
for u in units:
    seg = next(s for s in seg_records if s["label"] == u["unit"])
    u.update({"byte_start": seg["byte_start"], "byte_end": seg["byte_end"],
              "base_start": seg["base_start"], "base_end": seg["base_end"]})

# ---- encode ----
ENC = {"00": "A", "01": "C", "10": "G", "11": "T"}
table = []
for byte in range(256):
    bits = f"{byte:08b}"
    table.append("".join(ENC[bits[i:i + 2]] for i in range(0, 8, 2)))
bases = "".join(table[b] for b in raw)
assert len(bases) == 4 * len(raw)

seq_path = LANE / "constitution-dna-full.txt"
with seq_path.open("w", encoding="ascii") as f:
    for i in range(0, len(bases), 60):
        f.write(bases[i:i + 60] + "\n")

sha_bases = hashlib.sha256(bases.encode("ascii")).hexdigest()
fig = {"source_file": str(SOURCE), "source_bytes": len(raw),
       "source_sha256": sha, "total_bases": len(bases),
       "sha256_base_stream": sha_bases, "units": units,
       "segments": seg_records, "cross_checks_vs_gutenberg_5": cross,
       "signers_counted": len(signer_lines)}
(LANE / "work").mkdir(exist_ok=True)
(LANE / "work/encoder.json").write_text(json.dumps(fig, indent=1), encoding="utf-8")
print(json.dumps({"source_bytes": len(raw), "source_sha256": sha,
                  "total_bases": len(bases), "sha256_base_stream": sha_bases,
                  "segments": len(seg_records), "units": len(units),
                  "signers": len(signer_lines),
                  "sequence_file_bytes": seq_path.stat().st_size}, indent=2))
