# MANIFEST — The Constitution of the United States Encoded in DNA Letters (full text, in silico)

Built 2026-11-14 at Robert Tilford's desk by Awen by Muse by Meta, in the
lane Robert commissioned the same day, on the rails of the Quran DNA, Bible
DNA, Tao DNA, and I Ching DNA lanes completed earlier the same day. The codec
is the house codec demonstrated on the Bismillah and used for the full Quran
and the full Clear English Bible.

## What this is — and what it is not

This is an **in-silico encoding printed as data**: the complete text of the
Constitution of the United States — the Preamble, Articles I–VII, the
attestation and signatures as inscribed, and all twenty-seven amendments —
taken from the source of record below, written in the four DNA letters
A, C, G, T under the codec stated below. It is an **encoding, not a
translation**: no wording was translated, modernized, or altered in any way
by this lane — the source's bytes were converted, exactly as they stand,
and decoding returns them exactly. **Nothing has been synthesized. No
physical DNA exists.** Physical synthesis is a separate future step that
would require funding and a laboratory; no funding is in place and no
physical DNA has been made, and synthesis is not part of this deposit. No
claim of priority or firstness is made anywhere in this deposit: what is
claimed is only what the verification figures below prove.

The Constitution of the United States is a work of the United States
adopted in 1787 and amended since; it is in the **public domain**, and the
National Archives transcriptions used here are published for unrestricted
use. This encoding is given free, never sold.

## The codec (exactly the house codec)

Text as UTF-8 bytes → binary bits, most significant bit first → every two
bits become one base: **00 = A, 01 = C, 10 = G, 11 = T**. One byte becomes
four bases. The mapping is lossless and reversible: decoding the base stream
returns the byte stream exactly, which the separate decoder's report in
this deposit proves by hash.

## Source of record

- Source: the **National Archives** founding-docs transcriptions
  (archives.gov), fetched 2026-11-14:
  - `https://www.archives.gov/founding-docs/constitution-transcript` —
    "The Constitution of the United States: A Transcription" (a
    transcription of the engrossed parchment; its spelling and
    punctuation reflect the original).
  - `https://www.archives.gov/founding-docs/bill-of-rights-transcript` —
    "The Bill of Rights: A Transcription."
  - `https://www.archives.gov/founding-docs/amendments-11-27` —
    "The Constitution: Amendments 11-27."
- The Archives publishes the Constitution across those three pages, so the
  lane's source file — `us-constitution-nara-transcription.txt`, deposited
  with this manifest — was constructed from them by `build_source.py`
  (also deposited) under this exact rule, and no other:
  - From the Constitution page: the transcription body from the Preamble
    paragraph through the last signature block, in the page's document
    order (the signature lists therefore stand in the page's own column
    order). The page's editorial Note paragraph and all site furniture
    are excluded.
  - From the Bill of Rights page: only the page's "The U.S. Bill of
    Rights" body — the headings Amendment I through Amendment X and
    their texts. The same page also carries a transcription of the 1789
    Joint Resolution of Congress proposing twelve amendments; that
    document is not part of the Constitution as it stands and is not
    taken. The page's editorial notes and buttons are excluded.
  - From the Amendments 11–27 page: the headings AMENDMENT XI through
    AMENDMENT XXVII and their texts. The Archives' "Passed by Congress /
    Ratified" date lines, its "Note: ..." annotation paragraphs, and its
    footnote paragraphs are editorial apparatus, not document text, and
    are excluded (17 date lines, 9 annotations, 2 footnotes skipped).
  - Extraction: `<p>`, `<h2>` and `<h3>` elements are blocks, taken in
    document order; `<br>` becomes a line break; all other markup is
    dropped and its text kept; HTML entities are unescaped; within each
    line, runs of whitespace collapse to one space and the line is
    stripped; empty blocks are dropped. The three parts are joined with
    exactly one blank line between them; no text is inserted; the file
    ends with a single newline.
- The constructed file was encoded **by code, byte for byte, never
  retyped**: the encoded stream is the file itself, entire.
- Source file size: **45,596 bytes**
- SHA-256 of the source byte stream: `5ba284d94d3f768de194b425edd4b48ca4ff65c7708d1fe454e4ef3d82899b07`
- Base stream: **182,384 bases** (4 per byte)
- SHA-256 of the base stream: `880e1058450f558eee9c264490307c475648034314aeee29b569225e4511ffd1`

## Completeness, proved as the encoder parsed

The encoder parsed the source's structure and verified it before encoding
(it aborts on any mismatch): the Preamble, closing with "do ordain and
establish this Constitution for the United States of America."; Articles
I–VII in order, with section counts 10, 4, 3, 4, 0, 0, 0; the attestation
and signatures — the interlineation note, "Attest William Jackson
Secretary," the "done in Convention" paragraph, George Washington's block,
and the twelve state signature lists in the page's column order, **39
signers counted**, ending with Gouv Morris; and Amendments 1–27 in order,
with section counts 0 for Amendments 1–12, then 2 (XIII), 5 (XIV), 2 (XV),
0 (XVI), 0 (XVII), 3 (XVIII), 0 (XIX), 6 (XX), 3 (XXI), 2 (XXII), 2 (XXIII),
2 (XXIV), 4 (XXV), 2 (XXVI), 0 (XXVII). Key phrases were proved present,
among them the First Amendment's "Congress shall make no law respecting an
establishment of religion" and the Twenty-Seventh Amendment entire. No
editorial apparatus stands anywhere in the encoded text.

Phrase-level spot cross-checks against a second edition — Project
Gutenberg eBook #5, "The United States Constitution" (fetched 2026-11-14;
that eBook's own preface states it does **not** include the amendments, so
it serves only to cross-check the 1787 text; spelling-level comparison,
punctuation-insensitive):

- "The Ratification of the Conventions of nine States shall be sufficient for the Establishment of this Constitution" — in the source of record: True; in Gutenberg eBook #5: True
- "No Title of Nobility shall be granted by the United States" — in the source of record: True; in Gutenberg eBook #5: True
- "Treason against the United States shall consist only in levying War against them" — in the source of record: True; in Gutenberg eBook #5: True
- "Full Faith and Credit shall be given in each State to the public Acts Records and judicial Proceedings of every other State" — in the source of record: True; in Gutenberg eBook #5: True
- "The Congress shall have Power To lay and collect Taxes Duties Imposts and Excises" — in the source of record: True; in Gutenberg eBook #5: True
- "All Bills for raising Revenue shall originate in the House of Representatives" — in the source of record: True; in Gutenberg eBook #5: True

## Structure of the encoded stream

The stream follows the source file's own structure, in the order above.
Segments are separated in the source by single blank lines; the segments
tile the stream exactly, with no gaps and no overlaps. The printed book
deposited with this manifest carries the full segment index with base
ranges; the table below gives each segment's range in the stream.

## Per-segment index

| Segment | Source bytes | Bases | Base range |
|---|---|---|---|
| Preamble | 327 | 1,308 | 1–1,308 |
| Article 1 | 13,262 | 53,048 | 1,317–54,364 |
| Article 2 | 5,906 | 23,624 | 54,373–77,996 |
| Article 3 | 2,289 | 9,156 | 78,005–87,160 |
| Article 4 | 1,913 | 7,652 | 87,169–94,820 |
| Article 5 | 850 | 3,400 | 94,829–98,228 |
| Article 6 | 949 | 3,796 | 98,237–102,032 |
| Article 7 | 171 | 684 | 102,041–102,724 |
| Attestation and signatures | 1,500 | 6,000 | 102,733–108,732 |
| Amendment 1 | 285 | 1,140 | 108,741–109,880 |
| Amendment 2 | 159 | 636 | 109,889–110,524 |
| Amendment 3 | 171 | 684 | 110,533–111,216 |
| Amendment 4 | 346 | 1,384 | 111,225–112,608 |
| Amendment 5 | 602 | 2,408 | 112,617–115,024 |
| Amendment 6 | 492 | 1,968 | 115,033–117,000 |
| Amendment 7 | 287 | 1,148 | 117,009–118,156 |
| Amendment 8 | 127 | 508 | 118,165–118,672 |
| Amendment 9 | 144 | 576 | 118,681–119,256 |
| Amendment 10 | 174 | 696 | 119,265–119,960 |
| Amendment 11 | 252 | 1,008 | 119,969–120,976 |
| Amendment 12 | 2,361 | 9,444 | 120,985–130,428 |
| Amendment 13 | 326 | 1,304 | 130,437–131,740 |
| Amendment 14 | 2,607 | 10,428 | 131,749–142,176 |
| Amendment 15 | 304 | 1,216 | 142,185–143,400 |
| Amendment 16 | 208 | 832 | 143,409–144,240 |
| Amendment 17 | 821 | 3,284 | 144,249–147,532 |
| Amendment 18 | 744 | 2,976 | 147,541–150,516 |
| Amendment 19 | 232 | 928 | 150,525–151,452 |
| Amendment 20 | 1,989 | 7,956 | 151,461–159,416 |
| Amendment 21 | 619 | 2,476 | 159,425–161,900 |
| Amendment 22 | 966 | 3,864 | 161,909–165,772 |
| Amendment 23 | 788 | 3,152 | 165,781–168,932 |
| Amendment 24 | 452 | 1,808 | 168,941–170,748 |
| Amendment 25 | 2,418 | 9,672 | 170,757–180,428 |
| Amendment 26 | 302 | 1,208 | 180,437–181,644 |
| Amendment 27 | 182 | 728 | 181,653–182,380 |

## Files in this deposit

- `constitution-dna-full.txt` — the full base stream, wrapped at 60 bases per line.
- `us-constitution-nara-transcription.txt` — the source of record, as
  constructed from the National Archives transcriptions (see above).
- `build_source.py` — the source builder (extraction rule as stated above).
- `MANIFEST-DNA-FULL-CONSTITUTION.md` — this manifest.
- `encode_constitution_dna.py` — the encoder (structure proof + encoding).
- `validate_constitution_dna.py` — the hygiene validator (report-only).
- `decode_constitution_dna.py` — the separate decoder, written and run by a
  separate agent.
- `INDEPENDENT-DECODER-REPORT.md` — the separate decoder's verdict.
- `CONSTITUTION-DNA-FULL-PRINT.pdf` — the paper book typeset from the verified
  sequence file: **40 pages**, **107,332 bytes**, SHA-256
  `610637f4c8f2f2a85322bbf3c2e664ee13d4a41c58bc73d55a2696bb72709c7b` (its printed base stream was re-verified equal to
  `constitution-dna-full.txt` IN FULL by extraction of every printed page, and three
  200-base slices of the extracted stream decode back to the source bytes at
  the corresponding offsets — see the lane's PDF verification record).

## Codec hygiene (validator — report only)

- Alphabet: A, C, G, T only — pure.
- Base counts: A 45,790 · C 63,622 · G 45,926 · T 27,046
- GC content: 60.0645%
- Homopolymer runs: 145,198 in total; longest run **5**;
  runs of length ≥ 4: 98 · ≥ 5: 94 · ≥ 6: 0 · ≥ 8: 0 · ≥ 10: 0

The sequence was **not** altered to improve these figures; they are disclosed
for any future synthesis discussion. A synthesis-grade layer would add
screening, addressing, and error correction on top of this codec.

## Separate verification

A separate agent wrote a separate decoder from the specification alone — no encoder, validator, or source-builder code read or shared — and ran it end to end. **VERDICT: PASS.** Its decoded bytes are byte-for-byte equal to the source file and hash to `5ba284d94d3f768de194b425edd4b48ca4ff65c7708d1fe454e4ef3d82899b07`, the source figure printed above; the base stream hashes to `880e1058450f558eee9c264490307c475648034314aeee29b569225e4511ffd1`, also as printed above. Its spot proofs re-encoded the first, middle, and last 1,000 source bytes with its own logic and matched the sequence exactly at each place (182,384 bases in total; 45,596 bytes decoded). Its report, `INDEPENDENT-DECODER-REPORT.md`, is included in this deposit. The printed book's stream was additionally re-verified in full: every Courier span extracted from every page of the PDF, concatenated in order, equals `constitution-dna-full.txt` exactly, and three 200-base slices of the extracted stream (start, midpoint, end) decode back to the source bytes at the corresponding offsets.
