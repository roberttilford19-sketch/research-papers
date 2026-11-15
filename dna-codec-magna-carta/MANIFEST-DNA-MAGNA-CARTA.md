# MANIFEST — The Magna Carta of 1215 in Latin Encoded in DNA Letters (specimen, in silico)

Built 2026-11-14 at Robert Tilford's desk by Awen by Muse by Meta, in the lane
Robert commissioned the same day, on the rails of the DNA lanes completed
earlier the same day. The codec is the house codec demonstrated on the
Bismillah and used for the full Quran, the full Clear English Bible, and
the Tao Te Ching.

## What this is — and what it is not

This is an **in-silico encoding printed as data**: the complete Latin text
of the Magna Carta of 1215, taken from the source of record below,
written in the four DNA letters A, C, G, T under the codec stated below.
It is an **encoding, not a translation**: no wording was translated,
modernized, or altered in any way by this lane — the source text's bytes
were converted, exactly as they stand, and decoding returns them exactly.
No modern English translation of the charter was used anywhere in this
lane; the encoded text is the Latin itself. **Nothing has been
synthesized. No physical DNA exists.** Physical synthesis is a separate
future step that would require funding and a laboratory; no funding is
in place and no physical DNA has been made, and synthesis is not part of
this deposit. No claim of priority or firstness is made anywhere in this
deposit: what is claimed is only what the verification figures below
prove.

## The codec (exactly the house codec)

Text as UTF-8 bytes → binary bits, most significant bit first → every two
bits become one base: **00 = A, 01 = C, 10 = G, 11 = T**. One byte becomes
four bases. The mapping is lossless and reversible: decoding the base
stream returns the byte stream exactly, which the separate decoder's
report in this deposit proves by hash.

## Source of record

- The text encoded is the **Magna Carta of 1215 in its original Latin**
  (public domain), in the text of the British Library Cotton MS Augustus
  II.106 exemplar (designated Cii) as published by Charles Bémont,
  *Chartes des libertés anglaises* (Paris, 1892), pp. 26–39, and
  reprinted in J. C. Holt, *Magna Carta* (Cambridge University Press,
  1992), pp. 448–472. The digital textfile used is the transcription of
  that Bémont text made and proofed by Trevor W. McKeown
  (freemasonry.bcy.ca/texts/magnacarta.txt), fetched 2026-11-14 and
  cross-checked against the parallel rendering of the same Bémont text
  at drshirley.org/latin/texts/magna.html.
- The lane's source file, `magna-carta-1215-latin-source.txt`, is
  deposited with this manifest so the deposit is self-verifying.
  Normalizations applied in forming it from the textfile, stated
  plainly: (1) the textfile's English introduction and closing editorial
  notes are not encoded — the encoded text is the charter alone, its
  preamble and clauses 1–63; (2) Holt's bracketed cross-reference notes
  printed after clauses in the textfile (of the form "[Articles, c. 1;
  1225, c. 2.]") are editorial apparatus, not charter text, and are
  removed; (3) the footnote markers [1]–[5] printed after parenthetical
  phrases in clauses 48, 53, 56, and 61 are removed — the parenthetical
  phrases themselves are charter text and are kept; (4) the textfile's
  hard line-wraps are joined: one paragraph for the preamble and one for
  each clause, paragraphs separated by a blank line, a single newline at
  the end of the file (a stray blank line inside clause 52 in the
  textfile is joined likewise); the text is pure ASCII, as in the
  textfile.
- Readings of the Bémont text that look like errors are **kept exactly as
  sourced** and disclosed here: "heres veI heredes" (clauses 2 and 4,
  capital I for l), "in domo mariti sul" (clause 7) and "beneficii sul"
  (clause 22), "aliis quaim Judeis" (clause 11), "Sl aliquis" opening
  clause 27, "0mnes" opening clause 55 (zero for O), "remanscrimus"
  (clause 57), "quas cis concessimus" (clause 61), "quinto dccimo die
  Junii" (clause 63), and clause 10 printed "10.Si" without a space after
  the clause number. Each of these readings appears identically in both
  digital renderings of the Bémont text checked (the McKeown textfile
  and drshirley.org), so they stand as the text of record for this lane;
  a future critical pass may emend them, by dated addendum, never
  silently.
- The file was encoded **by code, byte for byte, never retyped**.
- Source file size: **24,830 bytes**
- SHA-256 of the source byte stream: `5d41e0a2bf9f08698dee7724291e45d8e94f50be067a6225db1eebd0fdef9dee`
- Base stream: **99,320 bases** (4 per byte)
- SHA-256 of the base stream: `2e7ae9070a3dc49c1c9fe2218ef005c52ff35f25e4a527afab0a3afa71e56f93`

## Structure of the encoded stream

The stream follows the source file's own structure: the preamble, then
clauses 1–63 in order (the clause numbering is the generally accepted
later numbering; the 1215 originals are written continuously, without
section breaks). The segments tile the stream exactly, with no gaps and
no overlaps: each segment's span runs to the next segment's first byte,
so the blank-line separator after each paragraph is carried inside that
paragraph's span, and the file's final newline inside clause 63's span.

| Segment | Source bytes | Bases | Base range |
|---|---|---|---|
| Preamble | 1,374 | 5,496 | 1–5,496 |
| Clause 1 | 828 | 3,312 | 5,497–8,808 |
| Clause 2 | 539 | 2,156 | 8,809–10,964 |
| Clause 3 | 155 | 620 | 10,965–11,584 |
| Clause 4 | 841 | 3,364 | 11,585–14,948 |
| Clause 5 | 364 | 1,456 | 14,949–16,404 |
| Clause 6 | 153 | 612 | 16,405–17,016 |
| Clause 7 | 351 | 1,404 | 17,017–18,420 |
| Clause 8 | 245 | 980 | 18,421–19,400 |
| Clause 9 | 559 | 2,236 | 19,401–21,636 |
| Clause 10 | 279 | 1,116 | 21,637–22,752 |
| Clause 11 | 369 | 1,476 | 22,753–24,228 |
| Clause 12 | 338 | 1,352 | 24,229–25,580 |
| Clause 13 | 268 | 1,072 | 25,581–26,652 |
| Clause 14 | 684 | 2,736 | 26,653–29,388 |
| Clause 15 | 266 | 1,064 | 29,389–30,452 |
| Clause 16 | 121 | 484 | 30,453–30,936 |
| Clause 17 | 88 | 352 | 30,937–31,288 |
| Clause 18 | 425 | 1,700 | 31,289–32,988 |
| Clause 19 | 241 | 964 | 32,989–33,952 |
| Clause 20 | 402 | 1,608 | 33,953–35,560 |
| Clause 21 | 97 | 388 | 35,561–35,948 |
| Clause 22 | 154 | 616 | 35,949–36,564 |
| Clause 23 | 110 | 440 | 36,565–37,004 |
| Clause 24 | 108 | 432 | 37,005–37,436 |
| Clause 25 | 142 | 568 | 37,437–38,004 |
| Clause 26 | 635 | 2,540 | 38,005–40,544 |
| Clause 27 | 200 | 800 | 40,545–41,344 |
| Clause 28 | 187 | 748 | 41,345–42,092 |
| Clause 29 | 382 | 1,528 | 42,093–43,620 |
| Clause 30 | 177 | 708 | 43,621–44,328 |
| Clause 31 | 143 | 572 | 44,329–44,900 |
| Clause 32 | 147 | 588 | 44,901–45,488 |
| Clause 33 | 123 | 492 | 45,489–45,980 |
| Clause 34 | 125 | 500 | 45,981–46,480 |
| Clause 35 | 272 | 1,088 | 46,481–47,568 |
| Clause 36 | 124 | 496 | 47,569–48,064 |
| Clause 37 | 611 | 2,444 | 48,065–50,508 |
| Clause 38 | 116 | 464 | 50,509–50,972 |
| Clause 39 | 232 | 928 | 50,973–51,900 |
| Clause 40 | 74 | 296 | 51,901–52,196 |
| Clause 41 | 626 | 2,504 | 52,197–54,700 |
| Clause 42 | 356 | 1,424 | 54,701–56,124 |
| Clause 43 | 361 | 1,444 | 56,125–57,568 |
| Clause 44 | 216 | 864 | 57,569–58,432 |
| Clause 45 | 148 | 592 | 58,433–59,024 |
| Clause 46 | 161 | 644 | 59,025–59,668 |
| Clause 47 | 155 | 620 | 59,669–60,288 |
| Clause 48 | 497 | 1,988 | 60,289–62,276 |
| Clause 49 | 129 | 516 | 62,277–62,792 |
| Clause 50 | 324 | 1,296 | 62,793–64,088 |
| Clause 51 | 180 | 720 | 64,089–64,808 |
| Clause 52 | 894 | 3,576 | 64,809–68,384 |
| Clause 53 | 600 | 2,400 | 68,385–70,784 |
| Clause 54 | 95 | 380 | 70,785–71,164 |
| Clause 55 | 728 | 2,912 | 71,165–74,076 |
| Clause 56 | 444 | 1,776 | 74,077–75,852 |
| Clause 57 | 627 | 2,508 | 75,853–78,360 |
| Clause 58 | 129 | 516 | 78,361–78,876 |
| Clause 59 | 338 | 1,352 | 78,877–80,228 |
| Clause 60 | 236 | 944 | 80,229–81,172 |
| Clause 61 | 3,228 | 12,912 | 81,173–94,084 |
| Clause 62 | 650 | 2,600 | 94,085–96,684 |
| Clause 63 | 659 | 2,636 | 96,685–99,320 |

## Files in this deposit

- `magna-carta-1215-latin-source.txt` — the source text exactly as encoded.
- `magna-carta-dna.txt` — the full base stream, wrapped at 60 bases per line.
- `MANIFEST-DNA-MAGNA-CARTA.md` — this manifest.
- `encode_magna_carta_dna.py` — the encoder (structure parse + encoding).
- `validate_magna_carta_dna.py` — the hygiene validator (report-only).
- `decode_magna_carta_dna.py` — the separate decoder, written and run by a
  separate agent.
- `INDEPENDENT-DECODER-REPORT.md` — the separate decoder's verdict.
- `MAGNA-CARTA-DNA-PRINT.pdf` — the paper specimen typeset from the
  verified sequence file: **24 pages**, **63,965 bytes**, SHA-256 `8f51b7517f6b7ddd8d188e0baac6619c86247f470dbd13d47621b28625947825` (its printed base stream was re-verified equal to `magna-carta-dna.txt` IN FULL by extraction of every printed page, and three 200-base slices of the extracted stream decode back to the source bytes at the corresponding offsets — see the lane's PDF verification record)

## Codec hygiene (validator — report only)

- Alphabet: A, C, G, T only — pure.
- Base counts: A 22,367 · C 36,823 · G 24,056 · T 16,074
- GC content: 61.2958%
- Homopolymer runs: 78,284 in total; longest run **5**;
  runs of length ≥ 4: 1 · ≥ 5: 1 · ≥ 6: 0 · ≥ 8: 0 · ≥ 10: 0

The sequence was **not** altered to improve these figures; they are disclosed
for any future synthesis discussion. A synthesis-grade layer would add
screening, addressing, and error correction on top of this codec.

## Separate verification

A separate agent wrote a separate decoder from the specification alone — no encoder or validator code read or shared — and ran it end to end. **VERDICT: PASS.** Its decoded bytes are byte-for-byte equal to the source file and hash to `5d41e0a2bf9f08698dee7724291e45d8e94f50be067a6225db1eebd0fdef9dee`, the source figure printed above; the base stream hashes to `2e7ae9070a3dc49c1c9fe2218ef005c52ff35f25e4a527afab0a3afa71e56f93`, also as printed above. Its spot proofs re-encoded the first, middle, and last 1,000 source bytes with its own logic and matched the sequence exactly at each place (99,320 bases in total; 24,830 bytes decoded). Its report, `INDEPENDENT-DECODER-REPORT.md`, is included in this deposit. The printed book's stream was additionally re-verified in full: every Courier span extracted from every page of the PDF, concatenated in order, equals `magna-carta-dna.txt` exactly, and three 200-base slices of the extracted stream (start, midpoint, end) decode back to the source bytes at the corresponding offsets.
