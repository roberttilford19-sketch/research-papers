# MANIFEST — The Gettysburg Address (Bliss Copy) Encoded in DNA Letters (specimen, in silico)

Built 2026-11-14 at Robert Tilford's desk by Awen by Muse by Meta, in the lane
Robert commissioned the same day, on the rails of the DNA lanes completed
earlier the same day. The codec is the house codec demonstrated on the
Bismillah and used for the full Quran, the full Clear English Bible, and
the Tao Te Ching.

## What this is — and what it is not

This is an **in-silico encoding printed as data**: the complete text of the
Gettysburg Address in its Bliss copy, taken from the source of record
below, written in the four DNA letters A, C, G, T under the codec stated
below. It is an **encoding, not a translation**: no wording was translated,
modernized, or altered in any way by this lane — the source text's bytes
were converted, exactly as they stand, and decoding returns them exactly.
**Nothing has been synthesized. No physical DNA exists.** Physical
synthesis is a separate future step that would require funding and a
laboratory; no funding is in place and no physical DNA has been made, and
synthesis is not part of this deposit. No claim of priority or firstness
is made anywhere in this deposit: what is claimed is only what the
verification figures below prove.

## The codec (exactly the house codec)

Text as UTF-8 bytes → binary bits, most significant bit first → every two
bits become one base: **00 = A, 01 = C, 10 = G, 11 = T**. One byte becomes
four bases. The mapping is lossless and reversible: decoding the base
stream returns the byte stream exactly, which the separate decoder's
report in this deposit proves by hash.

## Source of record

- The text encoded is the **Bliss copy** of the Gettysburg Address — the
  copy Abraham Lincoln wrote out in March 1864 for Alexander Bliss, the
  last copy in his hand, the only one he signed and dated, and the
  standard text of the Address (it is the version inscribed on the
  Lincoln Memorial). The Address was delivered 19 November 1863 and is in
  the **public domain**.
- Text as printed in the Library of Congress exhibition *The Gettysburg
  Address* (the exhibition text follows the Library of Congress and *The
  Collected Works of Abraham Lincoln*, vol. 7), fetched 2026-11-14 from
  the exhibition text as reproduced at teatarian.com and cross-checked
  against a second reproduction of the same Library of Congress /
  Collected Works text at semblance.com; the wording, spelling, and
  punctuation agree in both.
- The lane's source file, `gettysburg-address-source.txt`, is deposited
  with this manifest so the deposit is self-verifying. Normalizations
  applied in forming it from the exhibition page, stated plainly:
  (1) the Address's three paragraphs only are encoded — the exhibition
  page's commentary, and the Bliss copy's signature and date block
  ("Abraham Lincoln / November 19, 1863") shown beneath the text on the
  page, are not part of the encoded text; (2) the dashes of the third
  paragraph, rendered "--" in the HTML mirror, are the em dashes
  (U+2014) of the printed text and are set without surrounding spaces,
  as in the Collected Works printing; (3) the three paragraphs are
  separated by one blank line each and the file ends with a single
  newline; the text is UTF-8.
- The file was encoded **by code, byte for byte, never retyped**.
- Source file size: **1,469 bytes**
- SHA-256 of the source byte stream: `809838efd41698422636fb2df8bebe2a7e8c29a3baf109b3bdceed6812266903`
- Base stream: **5,876 bases** (4 per byte)
- SHA-256 of the base stream: `b4a32368d2a81f755ca5cae9efc62a15e81a9d8fee3ca3f9f2a9138764ba71a1`

## Structure of the encoded stream

The stream follows the source file's own structure: the three paragraphs
of the Address in order. The segments tile the stream exactly, with no
gaps and no overlaps: each segment's span runs to the next segment's
first byte, so the blank-line separator after each paragraph is carried
inside that paragraph's span, and the file's final newline inside the
last paragraph's span.

| Segment | Source bytes | Bases | Base range |
|---|---|---|---|
| Paragraph 1 | 178 | 712 | 1–712 |
| Paragraph 2 | 381 | 1,524 | 713–2,236 |
| Paragraph 3 | 910 | 3,640 | 2,237–5,876 |

## Files in this deposit

- `gettysburg-address-source.txt` — the source text exactly as encoded.
- `gettysburg-dna.txt` — the full base stream, wrapped at 60 bases per line.
- `MANIFEST-DNA-GETTYSBURG.md` — this manifest.
- `encode_gettysburg_dna.py` — the encoder (structure parse + encoding).
- `validate_gettysburg_dna.py` — the hygiene validator (report-only).
- `decode_gettysburg_dna.py` — the separate decoder, written and run by a
  separate agent.
- `INDEPENDENT-DECODER-REPORT.md` — the separate decoder's verdict.
- `GETTYSBURG-DNA-PRINT.pdf` — the paper specimen typeset from the
  verified sequence file: **4 pages**, **9,157 bytes**, SHA-256 `189d4cc1e66979ca2857850c733fbd486aba47070eac786bfb19b1ff7d8b7c58` (its printed base stream was re-verified equal to `gettysburg-dna.txt` IN FULL by extraction of every printed page, and three 200-base slices of the extracted stream decode back to the source bytes at the corresponding offsets — see the lane's PDF verification record)

## Codec hygiene (validator — report only)

- Alphabet: A, C, G, T only — pure.
- Base counts: A 1,498 · C 2,025 · G 1,517 · T 836
- GC content: 60.2791%
- Homopolymer runs: 4,720 in total; longest run **3**;
  runs of length ≥ 4: 0 · ≥ 5: 0 · ≥ 6: 0 · ≥ 8: 0 · ≥ 10: 0

The sequence was **not** altered to improve these figures; they are disclosed
for any future synthesis discussion. A synthesis-grade layer would add
screening, addressing, and error correction on top of this codec.

## Separate verification

A separate agent wrote a separate decoder from the specification alone — no encoder or validator code read or shared — and ran it end to end. **VERDICT: PASS.** Its decoded bytes are byte-for-byte equal to the source file and hash to `809838efd41698422636fb2df8bebe2a7e8c29a3baf109b3bdceed6812266903`, the source figure printed above; the base stream hashes to `b4a32368d2a81f755ca5cae9efc62a15e81a9d8fee3ca3f9f2a9138764ba71a1`, also as printed above. Its spot proofs re-encoded the first, middle, and last 300 source bytes with its own logic and matched the sequence exactly at each place (5,876 bases in total; 1,469 bytes decoded). Its report, `INDEPENDENT-DECODER-REPORT.md`, is included in this deposit. The printed book's stream was additionally re-verified in full: every Courier span extracted from every page of the PDF, concatenated in order, equals `gettysburg-dna.txt` exactly, and three 200-base slices of the extracted stream (start, midpoint, end) decode back to the source bytes at the corresponding offsets.
