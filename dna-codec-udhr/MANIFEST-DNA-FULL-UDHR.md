# MANIFEST — The Universal Declaration of Human Rights Encoded in DNA Letters (full text, in silico)

Built 2026-11-15 at Robert Tilford's desk by Awen by Muse by Meta, in the lane
Robert commissioned the same day, on the rails of the DNA lanes completed
before it (Quran, Clear English Bible, Tao Te Ching, U.S. Constitution, and
the rest of the shelf). The codec is the house codec demonstrated on the
Bismillah and used across those lanes.

## What this is — and what it is not

This is an **in-silico encoding printed as data**: the complete text of the
Universal Declaration of Human Rights — preamble and all thirty articles —
taken from the source of record below, written in the four DNA letters
A, C, G, T under the codec stated below. It is an **encoding, not a
translation**: no wording was translated, modernized, or altered by this
lane — the source text's bytes were converted, exactly as they stand, and
decoding returns them exactly. **Nothing has been synthesized. No physical
DNA exists, and none is implied.** Physical synthesis is a separate future
step that would require funding and a laboratory; no funding is in place
and no physical DNA has been made, and synthesis is not part of this
deposit. No claim of priority or firstness is made anywhere in this
deposit: what is claimed is only what the verification figures below prove.
This deposit is **given free, never sold**.

## The codec (exactly the house codec)

Text as UTF-8 bytes → binary bits, most significant bit first → every two
bits become one base: **00 = A, 01 = C, 10 = G, 11 = T**. One byte becomes
four bases. The mapping is lossless and reversible: decoding the base stream
returns the byte stream exactly, which the separate decoder's report in
this deposit proves by hash.

## Source of record

- Source: the Universal Declaration of Human Rights as published on the
  United Nations' official page,
  https://www.un.org/en/about-us/universal-declaration-of-human-rights
  (read at the desk 2026-11-15).
- The source file `udhr-un-official-text.txt` was constructed by
  `build_source.py` under this rule: the page's Declaration text only (the
  page's introductory prose about the Declaration is not part of the
  source). The title line stands first; then the heading "Preamble" and the
  preamble's ten paragraphs (seven "Whereas" clauses, "Now, therefore,",
  "The General Assembly,", and the Proclaims paragraph); then Articles
  1–30, each under its "Article N" heading, numbered clauses kept as
  separate paragraphs beginning "1. ", "2. ", etc., exactly as the page
  prints them. Paragraphs are separated by one blank line; each paragraph
  is a single line (the page's wrapped lines joined with single spaces);
  the file ends with one trailing newline. The builder aborts on any
  structural mismatch, and the encoder re-verifies the built file against
  the figures below before encoding it.
- Source file size: **10,821 bytes**
- SHA-256 of the source byte stream: `bfd143dd10de856ef2c86becc2a97155d21810389813cef8c530e05b8ab085db`
- Base stream: **43,284 bases** (4 per byte)
- SHA-256 of the base stream: `059cb2d7b53e19511ee92763c6dea518edbf74c0590d3340e1bc3493f560742d`

## Structure of the encoded stream

The stream follows the source's own structure, parsed by code and verified
as it was parsed: the title, the Preamble, and Articles 1–30 in order. The
segments tile the source's block structure exactly, with no gaps and no
overlaps; the source file's single trailing newline stands after Article
30's segment as the stream's final byte (bases 43,281–43,284). Byte ranges
below are 1-based, inclusive; base ranges likewise.

| Section | Bytes | Bases |
|---|---|---|
| Title | 1–37 | 1–148 |
| Preamble | 40–2051 | 157–8204 |
| Article 1 | 2054–2234 | 8213–8936 |
| Article 2 | 2237–2763 | 8945–11052 |
| Article 3 | 2766–2839 | 11061–11356 |
| Article 4 | 2842–2965 | 11365–11860 |
| Article 5 | 2968–3073 | 11869–12292 |
| Article 6 | 3076–3162 | 12301–12648 |
| Article 7 | 3165–3427 | 12657–13708 |
| Article 8 | 3430–3606 | 13717–14424 |
| Article 9 | 3609–3685 | 14433–14740 |
| Article 10 | 3688–3898 | 14749–15592 |
| Article 11 | 3901–4429 | 15601–17716 |
| Article 12 | 4432–4681 | 17725–18724 |
| Article 13 | 4684–4889 | 18733–19556 |
| Article 14 | 4892–5175 | 19565–20700 |
| Article 15 | 5178–5340 | 20709–21360 |
| Article 16 | 5343–5802 | 21369–23208 |
| Article 17 | 5805–5960 | 23217–23840 |
| Article 18 | 5963–6268 | 23849–25072 |
| Article 19 | 6271–6509 | 25081–26036 |
| Article 20 | 6512–6654 | 26045–26616 |
| Article 21 | 6657–7130 | 26625–28520 |
| Article 22 | 7133–7485 | 28529–29940 |
| Article 23 | 7488–8043 | 29949–32172 |
| Article 24 | 8046–8181 | 32181–32724 |
| Article 25 | 8184–8720 | 32733–34880 |
| Article 26 | 8723–9492 | 34889–37968 |
| Article 27 | 9495–9838 | 37977–39352 |
| Article 28 | 9841–9994 | 39361–39976 |
| Article 29 | 9997–10582 | 39985–42328 |
| Article 30 | 10585–10820 | 42337–43280 |

## Codec hygiene (validator, report only)

From `validate_udhr_dna.py`, run separately (full report in
`work/VALIDATOR-REPORT.md`): alphabet pure A/C/G/T; base counts
A 10,452 · C 14,765 · G 11,483 · T 6,584; GC content 60.6413%;
**longest homopolymer run: 5**. These figures are disclosed facts about the
plain codec's output; the sequence was not altered to improve them.

## Miniatures deposited with this lane

Two formula miniatures, encoded and verified under the same codec by
`encode_miniatures.py` (sequences in `miniatures-dna.txt`, figures in
`work/miniatures.json`), each built from explicit codepoints:

1. **E=mc²** — codepoints U+0045 U+003D U+006D U+0063 U+00B2 (the squared
   sign is U+00B2). 6 UTF-8 bytes → **24 bases**.
   SHA-256 of the source bytes: `03b680eab659c430a16c7f515928d31a4e46fb60e668543ca4d080390bfd0aaf`
   SHA-256 of the base stream: `0d45f068089ded4e02add9d1b558caa01d6667f9dbcb105d5356cadf83d6e8fa`
   Longest homopolymer run: 2.
   Sequence: `CACCATTCCGTCCGATTAAGGTAG`

2. **The Schrödinger equation**, in the exact form **iℏ ∂Ψ/∂t = ĤΨ** —
   codepoints U+0069, U+0127, U+0020, U+2202, U+03A8, U+002F, U+2202,
   U+0074, U+0020, U+003D, U+0020, U+0048, U+0302, U+03A8. Two construction
   notes any future decoder must honor: **ℏ is U+0127** (LATIN SMALL LETTER
   H WITH STROKE) — not U+210F, the look-alike glyph a keyboard produces;
   and **Ĥ is not a precomposed character** — it is the letter H (U+0048)
   followed by U+0302 (COMBINING CIRCUMFLEX ACCENT), not U+0124.
   22 UTF-8 bytes → **88 bases**.
   SHA-256 of the source bytes: `e72e899bddab430c45f45589c189dcc3fa84be98d343af157ab58ebcfc50ffd9`
   SHA-256 of the base stream: `fd8b85b7f4075fb3e4fb18ba58fe45a485a9f2d76ab1042834e8640761a086ce`
   Longest homopolymer run: 4.
   Sequence: `CGGCTACAGGCTAGAATGAGGAGAGAAGTATGGGGAAGTTTGAGGAGAGAAGCTCAAGAAATTCAGAACAGATATAGAAGTATGGGGA`
