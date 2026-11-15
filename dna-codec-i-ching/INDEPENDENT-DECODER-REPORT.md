# Independent Decoder Report — I Ching Draft DNA Lane

Date: 2026-11-14

This report was produced by a separate decoder agent. The decoder script `decode_iching_dna.py` was written from the written specification alone; the files `encode_iching_dna.py`, `validate_iching_dna.py`, and everything under `~/workspace/dna-iching-2026-11-14/work/` were not read, imported, or copied.

## Codec

The sequence file holds a base stream wrapped at 60 bases per line; all whitespace was stripped before decoding. Each base is two bits: A=00, C=01, G=10, T=11. Four bases make one byte, most significant pair first. Spot proofs used a separately written re-encoder in the same script (each byte split into its four two-bit fields, most significant first, mapped 00→A, 01→C, 10→G, 11→T).

## Source of record

- Sequence file: `~/workspace/dna-iching-2026-11-14/iching-dna-full.txt`
- Source file: `~/workspace/dna-iching-2026-11-14/I-CHING-DRAFT-ASSEMBLY-352-OF-450.txt` (also accepted as the decoder's optional `argv[1]`; it is the default when no argument is given)
- Manifest: `~/workspace/dna-iching-2026-11-14/MANIFEST-DNA-ICHING-DRAFT.md`

## Figures computed

- Total bases (after stripping all whitespace): 1,104,764
- Expected base count: 1,104,764
- Alphabet observed: A, C, G, T (exactly that set, no other characters)
- Base count modulo 4: 0
- Decoded bytes: 276,191
- Source bytes: 276,191
- Expected source bytes: 276,191
- SHA-256 of the source byte stream (computed from the source file): `1a84b3b8b98e6614c738281d44c6da581a9bd38e3a4914e02fd1a5e3be49f225`
- SHA-256 of the decoded byte stream (computed from this decoder's output): `1a84b3b8b98e6614c738281d44c6da581a9bd38e3a4914e02fd1a5e3be49f225`
- SHA-256 of the base stream (computed from the whitespace-stripped bases as ASCII): `1b53bbd55814d2db17c117e04d0da911652bda914278087ab818082ed56fe2fd`
- SHA-256 of the source byte stream as printed in the manifest: `1a84b3b8b98e6614c738281d44c6da581a9bd38e3a4914e02fd1a5e3be49f225`
- SHA-256 of the base stream as printed in the manifest: `1b53bbd55814d2db17c117e04d0da911652bda914278087ab818082ed56fe2fd`

## Checks

### (a) Base count, alphabet, divisibility — PASS

Base count is 1,104,764, equal to the expected 1,104,764. The alphabet is exactly {A, C, G, T}. 1,104,764 is divisible by 4 (remainder 0), giving 276,191 complete four-base groups.

### (b) Full decode is valid UTF-8 — PASS

The full decoded stream of 276,191 bytes decoded as strict UTF-8 with no error.

### (c) Decoded bytes equal the assembly byte-for-byte — PASS

The decoded bytes equal the source file bytes exactly (276,191 bytes compared, no differences). SHA-256 of the decoded stream is `1a84b3b8b98e6614c738281d44c6da581a9bd38e3a4914e02fd1a5e3be49f225`, identical to SHA-256 of the source file, `1a84b3b8b98e6614c738281d44c6da581a9bd38e3a4914e02fd1a5e3be49f225`.

### (d) Manifest SHA-256 figures match computed values — PASS

The manifest's source figure `1a84b3b8b98e6614c738281d44c6da581a9bd38e3a4914e02fd1a5e3be49f225` matches both the computed source hash and the computed decoded hash. The manifest's base-stream figure `1b53bbd55814d2db17c117e04d0da911652bda914278087ab818082ed56fe2fd` matches the computed base-stream hash `1b53bbd55814d2db17c117e04d0da911652bda914278087ab818082ed56fe2fd`.

### (e) Spot proofs by independent re-encoding — PASS

Each window is 1,000 source bytes re-encoded with the separately written re-encoder and compared against the sequence slice at byte offset × 4 (offsets below are 0-based, inclusive):

- First: source bytes 0–999 against bases 0–3,999 — match.
- Middle: source bytes 137,595–138,594 against bases 550,380–554,379 — match. This window is centered on the file midpoint (byte offset 138,095, the floor of 276,191 / 2; the window runs 500 bytes before it through 499 bytes after it).
- Last: source bytes 275,191–276,190 against bases 1,100,764–1,104,763 — match.

All three 1,000-byte windows (3,000 bytes, 12,000 bases in total) matched exactly.

### (f) Component check against the manifest table — PASS

For each of the seven components, the decoded bytes were sliced at the component's byte range from the manifest table (1-based inclusive) and hashed; every slice length equals the table's byte count, every range length equals its byte count, and every hash matches the table:

1. `PILOT-HEXAGRAMS-01-02-DRAFT-2026-11-08.md` — bytes 1–12,894 (12,894 bytes) — SHA-256 `eb009c4a7b35c58f69005119e38ae8665510f6f062d692bd2b9cd8157f5b2033` — match.
2. `WAVE-4-DRAFT-HEXAGRAMS-03-10-DRAFT-2026-11-09.md` — bytes 12,895–46,499 (33,605 bytes) — SHA-256 `90438a63f4052f708edd2e5242124c7c6f6f2df965547f90269f9dbeedf227ab` — match.
3. `WAVE-4-DRAFT-HEXAGRAMS-11-18-DRAFT-2026-11-09.md` — bytes 46,500–85,334 (38,835 bytes) — SHA-256 `2f114612a600786e9894923be1ea0988cdf08e3abc360b6ba788f88e44f7842f` — match.
4. `WAVE-4-DRAFT-HEXAGRAMS-19-26-DRAFT-2026-11-09.md` — bytes 85,335–126,125 (40,791 bytes) — SHA-256 `0564efb41e99b593c384254398fc31fd4fe125bc64af24ac9bcb722920263527` — match.
5. `WAVE-4-DRAFT-HEXAGRAMS-27-34-DRAFT-2026-11-09.md` — bytes 126,126–168,844 (42,719 bytes) — SHA-256 `8c15b0ce695fb6e857dc60decfa0dc7c5578d95c508c2640ee1c978e3a95f849` — match.
6. `WAVE-4-DRAFT-HEXAGRAMS-35-42-DRAFT-2026-11-09.md` — bytes 168,845–215,239 (46,395 bytes) — SHA-256 `5fbd6dea06594330c697cb10a5841f8dcf41ac228e03d0649bdc5fb2dac30e3e` — match.
7. `WAVE-5-DRAFT-HEXAGRAMS-43-50-DRAFT-2026-11-11.md` — bytes 215,240–276,191 (60,952 bytes) — SHA-256 `eb8283e6e902e63efd7a92b038bb8e33dd7b8e59e7dc0faf26f23db4158cbb85` — match.

Component count: 7 of 7 verified. The seven ranges tile the full 276,191 bytes with no gaps (1 through 276,191).

## Verdict

All six checks (a)–(f) pass: the base stream decodes, under the stated codec, to exactly the source assembly byte-for-byte; both manifest SHA-256 figures reproduce from this decoder's own computation; the first, middle, and last 1,000-byte spot proofs re-encode to the corresponding sequence slices; and all seven component slices hash to the values in the manifest table.

VERDICT: PASS
