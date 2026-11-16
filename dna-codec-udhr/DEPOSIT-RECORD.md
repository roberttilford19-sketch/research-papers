# DEPOSIT RECORD — Universal Declaration of Human Rights DNA lane (2026-11-15)

- Status: **BUILT AND VERIFIED — NOT SHELVED.** Nothing has been uploaded,
  published, or committed anywhere. Shelving is Robert Tilford's separate
  word, as with every lane.
- Lane folder: `~/workspace/dna-udhr-2026-11-15/`
- Files: `udhr-un-official-text.txt` (source of record) · `build_source.py` ·
  `encode_udhr_dna.py` · `udhr-dna-full.txt` · `decode_udhr_dna.py` ·
  `validate_udhr_dna.py` · `encode_miniatures.py` · `decode_miniatures.py` ·
  `miniatures-dna.txt` · `MANIFEST-DNA-FULL-UDHR.md` ·
  `INDEPENDENT-DECODER-REPORT.md` · `work/` (encoder.json, validator.json,
  VALIDATOR-REPORT.md, miniatures.json)

## The face of this deposit (carried on the manifest as well)

This is an **encoding, not a translation**. It is a **letter sequence
only**: the text's UTF-8 bytes written in the four DNA letters under the
house codec. **No physical DNA exists, and none is implied**; no synthesis
has been performed or funded. No claim of priority or firstness is made.
The deposit is **given free, never sold**.

## UDHR — figures

- Source: the Universal Declaration of Human Rights (preamble + Articles
  1–30, complete) as published on the United Nations' official page:
  https://www.un.org/en/about-us/universal-declaration-of-human-rights
  (read 2026-11-15), constructed into `udhr-un-official-text.txt` by
  `build_source.py` under the construction rule stated on the manifest's
  face.
- Source: 10,821 bytes, SHA-256
  `bfd143dd10de856ef2c86becc2a97155d21810389813cef8c530e05b8ab085db`
  → 43,284 bases, base-stream SHA-256
  `059cb2d7b53e19511ee92763c6dea518edbf74c0590d3340e1bc3493f560742d`.
- Longest homopolymer run: **5** (validator, report only; GC 60.6413%).
- Independent decoder round trip: **PASS**, byte-for-byte, checks (a)–(e)
  all green (see INDEPENDENT-DECODER-REPORT.md).

## Miniatures — figures

1. **E=mc²** — the squared sign is U+00B2. 6 UTF-8 bytes → 24 bases.
   Source-bytes SHA-256
   `03b680eab659c430a16c7f515928d31a4e46fb60e668543ca4d080390bfd0aaf`;
   base-stream SHA-256
   `0d45f068089ded4e02add9d1b558caa01d6667f9dbcb105d5356cadf83d6e8fa`.
   Longest homopolymer run: 2. Independent decode: **PASS**, byte-identical.
   Sequence: `CACCATTCCGTCCGATTAAGGTAG`

2. **The Schrödinger equation**, in the exact form **iℏ ∂Ψ/∂t = ĤΨ**.
   Codepoints: U+0069, U+0127, U+0020, U+2202, U+03A8, U+002F, U+2202,
   U+0074, U+0020, U+003D, U+0020, U+0048, U+0302, U+03A8. Construction
   notes any future decoder must honor: ℏ is **U+0127** (LATIN SMALL
   LETTER H WITH STROKE), not the look-alike U+210F that a keyboard's
   glyph produces; and **Ĥ is the letter H (U+0048) followed by U+0302
   (COMBINING CIRCUMFLEX ACCENT)** — not the precomposed U+0124.
   22 UTF-8 bytes → 88 bases. Source-bytes SHA-256
   `e72e899bddab430c45f45589c189dcc3fa84be98d343af157ab58ebcfc50ffd9`;
   base-stream SHA-256
   `fd8b85b7f4075fb3e4fb18ba58fe45a485a9f2d76ab1042834e8640761a086ce`.
   Longest homopolymer run: 4. Independent decode: **PASS**, byte- and
   codepoint-identical.
   Sequence: `CGGCTACAGGCTAGAATGAGGAGAGAAGTATGGGGAAGTTTGAGGAGAGAAGCTCAAGAAATTCAGAACAGATATAGAAGTATGGGGA`

## Build note

The miniatures encoder's first pass caught, by its own codepoint guard,
two silent substitution traps — a typed ℏ is U+210F rather than the
specified U+0127, and a typed Ĥ is the precomposed U+0124 rather than
U+0048 + U+0302. Both strings were rebuilt from explicit codepoint lists
before encoding, and the independent decoder verifies the codepoints, not
just the bytes' round trip. The episode is recorded here because it is
exactly the failure this lane's guards exist to catch.

— Awen by Muse by Meta, at Robert's commission.

---
**Shelving addendum (2026-11-15, Robert's ruling — Decision 5, tap A):** Shelved the same evening to roberttilford19-sketch/research-papers (branch main), folder `dna-codec-udhr/`, by Git Data API on the then-current HEAD, following the pattern of the Constitution, Magna Carta, and poem lanes. Landed files: this record, `MANIFEST-DNA-FULL-UDHR.md`, `INDEPENDENT-DECODER-REPORT.md`, the source text (`udhr-un-official-text.txt`), both DNA files (`udhr-dna-full.txt`, `miniatures-dna.txt`), and the build/encode/decode/validate scripts. The `work/` folder stays home, per the pattern. Guard run before upload: the encoder, validator, and independent decoders were re-run at the desk and the figures match this record exactly (UDHR 10,821 bytes → 43,284 bases, source SHA-256 bfd143dd10de856ef2c86becc2a97155d21810389813cef8c530e05b8ab085db; miniatures 24 and 88 bases, all hashes matching, every decode PASS). This addendum supersedes the "NOT SHELVED" status line above. The commit hash is recorded in the desk's shelving report and day log; a record cannot carry its own commit hash.
