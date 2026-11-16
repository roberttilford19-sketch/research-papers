# Independent Decoder Report — UDHR DNA Lane

Date: 2026-11-15

These decoder scripts were written from the specification alone. The
following files were not read, imported, or copied: `encode_udhr_dna.py`,
`encode_miniatures.py`, `validate_udhr_dna.py`, `build_source.py`, and
anything under `~/workspace/dna-udhr-2026-11-15/work/`.

## Codec

- Sequence file: `~/workspace/dna-udhr-2026-11-15/udhr-dna-full.txt` — base
  stream wrapped at 60 bases per line; all whitespace stripped before
  decoding.
- Mapping: A=00, C=01, G=10, T=11.
- Four bases make one byte, most significant pair first.
- Re-encoder for spot proofs was written separately in the same script,
  using independent bit-mask extraction logic.
- Miniatures: `miniatures-dna.txt`, one "key: SEQUENCE" line each, decoded
  under the same mapping and compared against the strings rebuilt from
  their specified codepoints.

Decoder scripts: `~/workspace/dna-udhr-2026-11-15/decode_udhr_dna.py`,
`~/workspace/dna-udhr-2026-11-15/decode_miniatures.py`

## Source of Record

- Source file: `~/workspace/dna-udhr-2026-11-15/udhr-un-official-text.txt`
  (the Universal Declaration of Human Rights as published at
  https://www.un.org/en/about-us/universal-declaration-of-human-rights,
  constructed under the rule stated on the manifest's face)
- Manifest: `~/workspace/dna-udhr-2026-11-15/MANIFEST-DNA-FULL-UDHR.md`

## Figures Computed — UDHR

- Total bases: 43284
- Expected base count: 43284
- Alphabet: {A, C, G, T}
- Decoded bytes: 10821
- Source bytes: 10821
- SHA-256 of the decoded byte stream: `bfd143dd10de856ef2c86becc2a97155d21810389813cef8c530e05b8ab085db`
- SHA-256 of the source byte stream (computed): `bfd143dd10de856ef2c86becc2a97155d21810389813cef8c530e05b8ab085db`
- SHA-256 of the base stream (computed, stripped ASCII bases): `059cb2d7b53e19511ee92763c6dea518edbf74c0590d3340e1bc3493f560742d`
- SHA-256 of the source byte stream (from manifest): `bfd143dd10de856ef2c86becc2a97155d21810389813cef8c530e05b8ab085db`
- SHA-256 of the base stream (from manifest): `059cb2d7b53e19511ee92763c6dea518edbf74c0590d3340e1bc3493f560742d`

## Checks — UDHR

- (a) Base count, alphabet, divisibility — PASS: base count 43284 equals expected 43284; alphabet exactly {A, C, G, T}; 43284 divisible by 4 with remainder 0 (43284 / 4 = 10821).
- (b) Full decode is valid UTF-8 — PASS: decoded 10821 bytes decoded as UTF-8 without error.
- (c) Decoded bytes equal source byte-for-byte and SHA-256 matches — PASS: decoded bytes 10821 equal source bytes 10821 byte-for-byte (equality true); SHA-256 decoded `bfd143dd10de856ef2c86becc2a97155d21810389813cef8c530e05b8ab085db` equals SHA-256 source computed `bfd143dd10de856ef2c86becc2a97155d21810389813cef8c530e05b8ab085db`.
- (d) Both manifest SHA-256 figures match computed values — PASS: manifest source SHA `bfd143dd10de856ef2c86becc2a97155d21810389813cef8c530e05b8ab085db` matches computed source SHA; manifest base SHA `059cb2d7b53e19511ee92763c6dea518edbf74c0590d3340e1bc3493f560742d` matches computed base SHA.
- (e) Spot proofs — PASS: re-encoded with independent logic and compared against sequence slices at byte offset × 4. First: source byte offset 0, 1000 bytes, base offset 0, 4000 bases, match true. Middle (centered on file midpoint 5410): source byte offset 4910, 1000 bytes, base offset 19640, 4000 bases, match true. Last: source byte offset 9821, 1000 bytes, base offset 39284, 4000 bases, match true. All three spots matched.

## Figures and Checks — Miniatures

- **E=mc²** — 24 bases, decoded 6 bytes, byte-identical to the UTF-8 of the
  specified string (codepoints U+0045 U+003D U+006D U+0063 U+00B2): PASS.
  SHA-256 decoded bytes `03b680eab659c430a16c7f515928d31a4e46fb60e668543ca4d080390bfd0aaf`;
  SHA-256 base stream `0d45f068089ded4e02add9d1b558caa01d6667f9dbcb105d5356cadf83d6e8fa` —
  both equal the encoder's and manifest's figures.
- **iℏ ∂Ψ/∂t = ĤΨ** — 88 bases, decoded 22 bytes, byte-identical and
  codepoint-identical to the specified string (U+0069 U+0127 U+0020 U+2202
  U+03A8 U+002F U+2202 U+0074 U+0020 U+003D U+0020 U+0048 U+0302 U+03A8):
  PASS. The decode confirms ℏ is U+0127 (not U+210F) and Ĥ is U+0048 +
  U+0302 (not the precomposed U+0124). SHA-256 decoded bytes
  `e72e899bddab430c45f45589c189dcc3fa84be98d343af157ab58ebcfc50ffd9`;
  SHA-256 base stream `fd8b85b7f4075fb3e4fb18ba58fe45a485a9f2d76ab1042834e8640761a086ce` —
  both equal the encoder's and manifest's figures.

## Verdict

All checks (a)–(e) passed for the UDHR stream, and both miniatures decode
byte-for-byte to their specified strings. The independent decoders, written
from the specification alone, reproduce the source exactly from the base
streams, and both manifest SHA-256 figures match the computed values.

VERDICT: PASS
