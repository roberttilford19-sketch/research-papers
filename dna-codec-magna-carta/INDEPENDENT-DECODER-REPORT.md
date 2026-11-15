# Independent Decoder Report — Magna Carta DNA Lane

Date: 2026-11-14

This decoder was written from the specification alone. The following files were not read, imported, or copied: `~/workspace/dna-magna-carta-2026-11-14/encode_magna_carta_dna.py`, `~/workspace/dna-magna-carta-2026-11-14/validate_magna_carta_dna.py`, and anything under `~/workspace/dna-magna-carta-2026-11-14/work/`. The decoder is `~/workspace/dna-magna-carta-2026-11-14/decode_magna_carta_dna.py`, written independently from the specification stated for this lane.

## Codec

As implemented in the independent decoder:

- The sequence file is read as text and all whitespace is stripped, yielding the stripped base stream.
- Each base is two bits: A=00, C=01, G=10, T=11.
- Four bases make one byte, most significant pair first: the first base contributes the two most significant bits, the second the next two, the third the next two, and the fourth the two least significant bits.
- The decoded byte stream should equal the source file's bytes exactly.
- The base-stream SHA-256 is taken over the stripped base stream's ASCII bytes.

For the spot proofs in check (e), a separately written re-encoder inside the same script uses independent bit-extraction logic: for each byte it extracts two bits at a time by shifting (6, 4, 2, 0) and masking with 0b11, mapping 0→A, 1→C, 2→G, 3→T via an indexed tuple, rather than reusing the decoder's table or grouping logic.

## Source of Record

- Sequence file: `~/workspace/dna-magna-carta-2026-11-14/magna-carta-dna.txt`
- Source file: `~/workspace/dna-magna-carta-2026-11-14/magna-carta-1215-latin-source.txt`
- Manifest: `~/workspace/dna-magna-carta-2026-11-14/MANIFEST-DNA-MAGNA-CARTA.md`
- Decoder: `~/workspace/dna-magna-carta-2026-11-14/decode_magna_carta_dna.py`

## Figures Computed

- Total bases: 99320
- Expected base count: 99320
- Alphabet: A, C, G, T (exactly {A, C, G, T})
- Decoded bytes: 24830
- Source bytes: 24830
- SHA-256 of decoded stream: `5d41e0a2bf9f08698dee7724291e45d8e94f50be067a6225db1eebd0fdef9dee`
- SHA-256 of source (computed): `5d41e0a2bf9f08698dee7724291e45d8e94f50be067a6225db1eebd0fdef9dee`
- SHA-256 of base stream (computed): `2e7ae9070a3dc49c1c9fe2218ef005c52ff35f25e4a527afab0a3afa71e56f93`
- SHA-256 of source as printed in the manifest: `5d41e0a2bf9f08698dee7724291e45d8e94f50be067a6225db1eebd0fdef9dee`
- SHA-256 of base stream as printed in the manifest: `2e7ae9070a3dc49c1c9fe2218ef005c52ff35f25e4a527afab0a3afa71e56f93`

## Checks

- (a) PASS — Base count 99320 equals the expected count 99320; alphabet is exactly {A, C, G, T}; 99320 is divisible by 4 (99320 / 4 = 24830).
- (b) PASS — The full decode of 24830 bytes is valid UTF-8 (decoded with no UnicodeDecodeError).
- (c) PASS — Decoded bytes (24830) equal the source file byte-for-byte (24830 bytes), and SHA-256(decoded) `5d41e0a2bf9f08698dee7724291e45d8e94f50be067a6225db1eebd0fdef9dee` equals SHA-256(source as read from disk) `5d41e0a2bf9f08698dee7724291e45d8e94f50be067a6225db1eebd0fdef9dee`.
- (d) PASS — Both SHA-256 figures parsed from the manifest match the computed values: source manifest `5d41e0a2bf9f08698dee7724291e45d8e94f50be067a6225db1eebd0fdef9dee` equals computed source `5d41e0a2bf9f08698dee7724291e45d8e94f50be067a6225db1eebd0fdef9dee`; base-stream manifest `2e7ae9070a3dc49c1c9fe2218ef005c52ff35f25e4a527afab0a3afa71e56f93` equals computed base-stream `2e7ae9070a3dc49c1c9fe2218ef005c52ff35f25e4a527afab0a3afa71e56f93` (over the stripped bases as ASCII).
- (e) PASS — Spot proofs with the separately written re-encoder all matched the sequence at byte-offset × 4: first 1000 source bytes at byte offset 0 (base offset 0) matched; a 1000-byte chunk centered on the file midpoint at byte offset 11915 (midpoint 12415 minus 500; base offset 47660) matched; last 1000 source bytes at byte offset 23830 (base offset 95320) matched.

## Verdict

All checks (a)–(e) passed: the base count, alphabet, and divisibility are correct; the decode is valid UTF-8; the decoded bytes equal the source byte-for-byte with matching SHA-256; both manifest SHA-256 figures match the computed values; and all three spot re-encodings match the sequence.

VERDICT: PASS
