# Independent Decoder Report — Tao Te Ching DNA Lane

Date: 2026-11-14

This decoder script was written from the specification alone. The following files were not read, imported, or copied: `encode_tao_dna.py`, `validate_tao_dna.py`, and anything under `~/workspace/dna-tao-2026-11-14/work/`.

## Codec

- Sequence file: `~/workspace/dna-tao-2026-11-14/tao-dna-full.txt` — base stream wrapped at 60 bases per line; all whitespace stripped before decoding.
- Mapping: A=00, C=01, G=10, T=11.
- Four bases make one byte, most significant pair first.
- Re-encoder for spot proofs was written separately in the same script, using independent bit-mask extraction logic.

Decoder script: `~/workspace/dna-tao-2026-11-14/decode_tao_dna.py`

## Source of Record

- Source file: `~/workspace/your_files/TAO-TE-CHING-THE-TILFORD-TRANSLATION-DRAFT-2026-10-31.md`
- Manifest: `~/workspace/dna-tao-2026-11-14/MANIFEST-DNA-FULL-TAO.md`

## Figures Computed

- Total bases: 303148
- Expected base count: 303148
- Alphabet: {A, C, G, T}
- Decoded bytes: 75787
- Source bytes: 75787
- SHA-256 of the decoded byte stream: `2a73e08bd0599e0de6f30e9f68b0dcbb3746ccd1b2a0c56937336c8741a111f1`
- SHA-256 of the source byte stream (computed): `2a73e08bd0599e0de6f30e9f68b0dcbb3746ccd1b2a0c56937336c8741a111f1`
- SHA-256 of the base stream (computed, stripped ASCII bases): `0e9084409832e69e0359c416089c89ebac98785bebe3bf96c348b756ec4ea4cd`
- SHA-256 of the source byte stream (from manifest): `2a73e08bd0599e0de6f30e9f68b0dcbb3746ccd1b2a0c56937336c8741a111f1`
- SHA-256 of the base stream (from manifest): `0e9084409832e69e0359c416089c89ebac98785bebe3bf96c348b756ec4ea4cd`

## Checks

- (a) Base count, alphabet, divisibility — PASS: base count 303148 equals expected 303148; alphabet exactly {A, C, G, T}; 303148 divisible by 4 with remainder 0 (303148 / 4 = 75787).
- (b) Full decode is valid UTF-8 — PASS: decoded 75787 bytes decoded as UTF-8 without error.
- (c) Decoded bytes equal source byte-for-byte and SHA-256 matches — PASS: decoded bytes 75787 equal source bytes 75787 byte-for-byte (equality true); SHA-256 decoded `2a73e08bd0599e0de6f30e9f68b0dcbb3746ccd1b2a0c56937336c8741a111f1` equals SHA-256 source computed `2a73e08bd0599e0de6f30e9f68b0dcbb3746ccd1b2a0c56937336c8741a111f1`.
- (d) Both manifest SHA-256 figures match computed values — PASS: manifest source SHA `2a73e08bd0599e0de6f30e9f68b0dcbb3746ccd1b2a0c56937336c8741a111f1` matches computed source SHA `2a73e08bd0599e0de6f30e9f68b0dcbb3746ccd1b2a0c56937336c8741a111f1`; manifest base SHA `0e9084409832e69e0359c416089c89ebac98785bebe3bf96c348b756ec4ea4cd` matches computed base SHA `0e9084409832e69e0359c416089c89ebac98785bebe3bf96c348b756ec4ea4cd`.
- (e) Spot proofs — PASS: re-encoded with independent logic and compared against sequence slices at byte offset × 4. First: source byte offset 0, 1000 bytes, base offset 0, 4000 bases, match true. Middle (centered on file midpoint 37893): source byte offset 37393, 1000 bytes, base offset 149572, 4000 bases, match true. Last: source byte offset 74787, 1000 bytes, base offset 299148, 4000 bases, match true. All three spots matched.

## Verdict

All checks (a)–(e) passed. The independent decoder, written from the specification alone, reproduces the source file exactly from the base stream, and both manifest SHA-256 figures match the computed values.

VERDICT: PASS
