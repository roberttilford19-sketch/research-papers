#!/usr/bin/env python3
"""SOURCE BUILDER — U.S. Constitution DNA lane (2026-11-14).
Constructs the lane's source of record from the National Archives
founding-docs transcriptions (fetched 2026-11-14, local copies in
source/):

  1. https://www.archives.gov/founding-docs/constitution-transcript
     -> the Preamble paragraph through the last signature block
        ("Gouv Morris"), in the page's document order. The page's
        editorial Note paragraph and all page furniture are excluded.
  2. https://www.archives.gov/founding-docs/bill-of-rights-transcript
     -> only the page's "The U.S. Bill of Rights" body: the headings
        "Amendment I" .. "Amendment X" and their texts. The same page
        also carries a transcription of the 1789 Joint Resolution
        proposing 12 amendments; that document is NOT part of the
        Constitution as it stands and is not taken. The page's
        editorial Note paragraphs and buttons are excluded.
  3. https://www.archives.gov/founding-docs/amendments-11-27
     -> "AMENDMENT XI" .. "AMENDMENT XXVII" and their texts. The
        Archives' "Passed by Congress / Ratified" date lines
        (<p class="smaller">), its "Note: ..." annotation paragraphs,
        and its footnote paragraphs (beginning "*") are editorial
        apparatus, not document text, and are excluded.

Extraction rule (deterministic): within each region, <p>, <h2> and <h3>
elements are blocks, taken in document order; <br> becomes a line
break; all other markup is dropped and its text kept; HTML entities
are unescaped; within each line, runs of whitespace collapse to one
space and the line is stripped; empty blocks are dropped. The three
parts are joined with exactly one blank line between them, no text is
inserted, and the file ends with a single newline. Output:
us-constitution-nara-transcription.txt (UTF-8)."""
import re, sys
from html.parser import HTMLParser
from pathlib import Path

LANE = Path.home() / "workspace/dna-constitution-2026-11-14"
SRC = LANE / "source"

class BlockExtractor(HTMLParser):
    BLOCK = {"p", "h2", "h3"}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []        # (text, tag, classes)
        self.cur = None         # [tag, classes, [chunks]]
    def handle_starttag(self, tag, attrs):
        if tag in self.BLOCK and self.cur is None:
            cls = dict(attrs).get("class", "")
            self.cur = [tag, cls, []]
        elif tag == "br" and self.cur is not None:
            self.cur[2].append("\n")
    def handle_startendtag(self, tag, attrs):
        if tag == "br" and self.cur is not None:
            self.cur[2].append("\n")
    def handle_endtag(self, tag):
        if self.cur is not None and tag == self.cur[0]:
            raw = "".join(self.cur[2])
            lines = []
            for ln in raw.split("\n"):
                ln = re.sub(r"\s+", " ", ln).strip()
                if ln:
                    lines.append(ln)
            text = "\n".join(lines)
            if text:
                self.blocks.append((text, self.cur[0], self.cur[1]))
            self.cur = None
    def handle_data(self, data):
        if self.cur is not None:
            self.cur[2].append(data)

def extract(html, start_marker, end_marker):
    i = html.find(start_marker)
    if i < 0:
        sys.exit(f"ABORT: start marker not found: {start_marker[:60]}")
    j = html.find(end_marker, i)
    if j < 0:
        sys.exit(f"ABORT: end marker not found: {end_marker[:60]}")
    region = html[i:j + len(end_marker)]
    p = BlockExtractor()
    p.feed(region)
    p.close()
    if p.cur is not None:
        sys.exit("ABORT: unterminated block at region end")
    return p.blocks

def main():
    const_html = (SRC / "nara-constitution-transcript.html").read_text(encoding="utf-8")
    bor_html = (SRC / "nara-bill-of-rights-transcript.html").read_text(encoding="utf-8")
    amd_html = (SRC / "nara-amendments-11-27.html").read_text(encoding="utf-8")

    part1 = extract(const_html, '<p><span class="larger">', 'Gouv Morris</a></p>')
    part2 = extract(bor_html, '<h3>Amendment I</h3>',
                    'are reserved to the States respectively, or to the people.</p>')
    part3_raw = extract(amd_html, '<h3><a id="xi" name="xi"></a>AMENDMENT XI</h3>',
                        'shall have intervened.</p>')
    skipped = []
    part3 = []
    for text, tag, cls in part3_raw:
        if tag == "p" and "smaller" in cls:
            skipped.append(("date-line", text[:60]))
            continue
        if text.startswith("*"):
            skipped.append(("footnote", text[:60]))
            continue
        if tag == "p" and text.startswith("Note:"):
            skipped.append(("annotation", text[:60]))
            continue
        part3.append((text, tag, cls))

    for name, part in (("PART 1 (Constitution)", part1),
                       ("PART 2 (Bill of Rights)", part2),
                       ("PART 3 (Amendments 11-27)", part3)):
        print(f"== {name}: {len(part)} blocks")
        for text, tag, cls in part:
            first = text.split("\n")[0]
            print(f"  [{tag}] {first[:95]}")
    print("== SKIPPED from part 3:", skipped)

    texts = ["\n\n".join(t for t, _, _ in part) for part in (part1, part2, part3)]
    out = "\n\n".join(texts) + "\n"
    target = LANE / "us-constitution-nara-transcription.txt"
    target.write_text(out, encoding="utf-8")
    print("WROTE", target, len(out.encode("utf-8")), "bytes")

if __name__ == "__main__":
    main()
