# MANIFEST — The I Ching (The Tilford Translation, DRAFT) Encoded in DNA Letters (in silico)

Built 2026-11-14 at Robert Tilford's desk by Awen by Muse by Meta, in the lane
Robert commissioned the same day, on the rails of the Quran DNA and Bible DNA
lanes completed earlier the same day. The codec is the house codec demonstrated
on the Bismillah and used for the full Quran and the full Clear English Bible.

## DRAFT — IN PROGRESS — READ THIS FACE FIRST

This deposit encodes a **draft in progress, exactly as it stands** — not a
finished book, and no completeness claim is made anywhere in it. Robert
Tilford's I Ching translation stands today at:

- **352 of 450 units DRAFTED** (Hexagrams 1–50: the pilot, Hexagrams 1–2,
  plus six post-pilot batches of 56 units each, Hexagrams 3–50)
- **240 of 450 units APPROVED** (the pilot and the first four batches,
  approved 2026-11-09; the fifth batch is drafted and desk-graded, awaiting
  Robert's read; the sixth is drafted only)
- **98 of 450 units not yet drafted** (Hexagrams 51–64 and the Ten Wings
  apparatus are not in this stream at all)

The draft's own gates stand open on its face: DeepSeek collation happens
later, by Robert's hand, and the lane's Gate 3 requires review of the full
draft by an independent reviewer demonstrably expert in Classical Chinese
and the Zhouyi textual tradition before anything is called final. Encoding
this draft preserves it exactly as it stands today; it approves nothing,
collates nothing, reviews nothing, and publishes nothing beyond this shelf
deposit.

## The source, stated plainly

No single assembled master file of the I Ching draft exists on disk. The
draft of record is **seven files** in Robert's I Ching lane folder
(`iching/`). This lane assembled its source of record by **pure
concatenation** of those seven files' bytes in drafting order — nothing
added, nothing removed, nothing altered — and deposited that assembly
beside this manifest as `I-CHING-DRAFT-ASSEMBLY-352-OF-450.txt`. Every
component file's size and SHA-256 were verified before assembly and are
recorded below with its byte range, so any reader can split the decoded
stream back into the exact seven files and check each one.

| Component file | Hexagrams | Units | Status | Bytes | SHA-256 | Byte range in assembly | Base range |
|---|---|---|---|---|---|---|---|
| `PILOT-HEXAGRAMS-01-02-DRAFT-2026-11-08.md` | 1–2 | 16 | APPROVED (2026-11-09) | 12,894 | `eb009c4a7b35c58f69005119e38ae8665510f6f062d692bd2b9cd8157f5b2033` | 1–12,894 | 1–51,576 |
| `WAVE-4-DRAFT-HEXAGRAMS-03-10-DRAFT-2026-11-09.md` | 3–10 | 56 | APPROVED (2026-11-09) | 33,605 | `90438a63f4052f708edd2e5242124c7c6f6f2df965547f90269f9dbeedf227ab` | 12,895–46,499 | 51,577–185,996 |
| `WAVE-4-DRAFT-HEXAGRAMS-11-18-DRAFT-2026-11-09.md` | 11–18 | 56 | APPROVED (2026-11-09) | 38,835 | `2f114612a600786e9894923be1ea0988cdf08e3abc360b6ba788f88e44f7842f` | 46,500–85,334 | 185,997–341,336 |
| `WAVE-4-DRAFT-HEXAGRAMS-19-26-DRAFT-2026-11-09.md` | 19–26 | 56 | APPROVED (2026-11-09) | 40,791 | `0564efb41e99b593c384254398fc31fd4fe125bc64af24ac9bcb722920263527` | 85,335–126,125 | 341,337–504,500 |
| `WAVE-4-DRAFT-HEXAGRAMS-27-34-DRAFT-2026-11-09.md` | 27–34 | 56 | APPROVED (2026-11-09) | 42,719 | `8c15b0ce695fb6e857dc60decfa0dc7c5578d95c508c2640ee1c978e3a95f849` | 126,126–168,844 | 504,501–675,376 |
| `WAVE-4-DRAFT-HEXAGRAMS-35-42-DRAFT-2026-11-09.md` | 35–42 | 56 | DRAFTED, desk-graded 2026-11-09, awaiting Robert's read | 46,395 | `5fbd6dea06594330c697cb10a5841f8dcf41ac228e03d0649bdc5fb2dac30e3e` | 168,845–215,239 | 675,377–860,956 |
| `WAVE-5-DRAFT-HEXAGRAMS-43-50-DRAFT-2026-11-11.md` | 43–50 | 56 | DRAFTED ONLY — not graded, not read, not approved | 60,952 | `eb8283e6e902e63efd7a92b038bb8e33dd7b8e59e7dc0faf26f23db4158cbb85` | 215,240–276,191 | 860,957–1,104,764 |

## What this is — and what it is not

This is an **in-silico encoding printed as data**: the assembled draft of
record below, written in the four DNA letters A, C, G, T under the codec
stated below. It is an **encoding, not a translation**: no wording was
translated, modernized, or altered in any way by this lane — the draft's
bytes were converted, exactly as they stand, and decoding returns them
exactly. **Nothing has been synthesized. No physical DNA exists.** Physical
synthesis is a separate future step that would require funding and a
laboratory; no funding is in place and no physical DNA has been made, and
synthesis is not part of this deposit. No claim of priority or firstness
is made anywhere in this deposit: what is claimed is only what the
verification figures below prove.

## The codec (exactly the house codec)

Text as UTF-8 bytes → binary bits, most significant bit first → every two
bits become one base: **00 = A, 01 = C, 10 = G, 11 = T**. One byte becomes
four bases. The mapping is lossless and reversible: decoding the base stream
returns the byte stream exactly, which the separate decoder's report in
this deposit proves by hash.

## Source of record

- Assembly file: `I-CHING-DRAFT-ASSEMBLY-352-OF-450.txt` (deposited with
  this manifest; built by pure concatenation of the seven component files
  tabled above).
- The assembly was encoded **by code, byte for byte, never retyped**.
- Assembly size: **276,191 bytes**
- SHA-256 of the source byte stream: `1a84b3b8b98e6614c738281d44c6da581a9bd38e3a4914e02fd1a5e3be49f225`
- Base stream: **1,104,764 bases** (4 per byte)
- SHA-256 of the base stream: `1b53bbd55814d2db17c117e04d0da911652bda914278087ab818082ed56fe2fd`

## Structure of the encoded stream

The stream follows the assembly's own order: the seven component files in
drafting order, Hexagrams 1–50 in sequence inside them. The components
tile the stream exactly, with no gaps and no overlaps. Each hexagram's
range below runs from its heading to the next hexagram's heading, capped
at its own component file's end (a file's closing board therefore rides
inside its last hexagram's range). The printed book deposited with this
manifest carries the same indexes with first pages.

## Per-hexagram index

| Hexagram | Title | Source bytes | Base range |
|---|---|---|---|
| 1 | 乾 (Qián) | 1,906 | 4,781–12,404 |
| 2 | 坤 (Kūn) | 9,793 | 12,405–51,576 |
| 3 | 屯 (Zhùn) | 3,424 | 61,221–74,916 |
| 4 | 蒙 (Méng) | 2,582 | 74,917–85,244 |
| 5 | 需 (Xū) | 1,453 | 85,245–91,056 |
| 6 | 訟 (Sòng) | 2,939 | 91,057–102,812 |
| 7 | 師 (Shī) | 2,931 | 102,813–114,536 |
| 8 | 比 (Bǐ) | 2,871 | 114,537–126,020 |
| 9 | 小畜 (Xiǎoxù) | 1,976 | 126,021–133,924 |
| 10 | 履 (Lǚ) | 13,018 | 133,925–185,996 |
| 11 | 泰 (Tài) | 3,810 | 197,305–212,544 |
| 12 | 否 (Pǐ) | 4,229 | 212,545–229,460 |
| 13 | 同人 (Tóngrén) | 2,332 | 229,461–238,788 |
| 14 | 大有 (Dàyǒu) | 2,947 | 238,789–250,576 |
| 15 | 謙 (Qiān) | 2,332 | 250,577–259,904 |
| 16 | 豫 (Yù) | 3,026 | 259,905–272,008 |
| 17 | 隨 (Suí) | 2,825 | 272,009–283,308 |
| 18 | 蠱 (Gǔ) | 14,507 | 283,309–341,336 |
| 19 | 臨 (Lín) | 2,149 | 354,557–363,152 |
| 20 | 觀 (Guān) | 2,796 | 363,153–374,336 |
| 21 | 噬嗑 (Shìkè) | 3,059 | 374,337–386,572 |
| 22 | 賁 (Bì) | 2,314 | 386,573–395,828 |
| 23 | 剝 (Bō) | 3,840 | 395,829–411,188 |
| 24 | 復 (Fù) | 3,403 | 411,189–424,800 |
| 25 | 无妄 (Wúwàng) | 2,336 | 424,801–434,144 |
| 26 | 大畜 (Dàxù) | 17,589 | 434,145–504,500 |
| 27 | 頤 (Yí) | 3,907 | 514,665–530,292 |
| 28 | 大過 (Dàguò) | 2,499 | 530,293–540,288 |
| 29 | 習坎 (Xíkǎn) | 3,105 | 540,289–552,708 |
| 30 | 離 (Lí) | 2,794 | 552,709–563,884 |
| 31 | 咸 (Xián) | 2,641 | 563,885–574,448 |
| 32 | 恒 (Héng) | 2,551 | 574,449–584,652 |
| 33 | 遯 (Dùn) | 2,519 | 584,653–594,728 |
| 34 | 大壯 (Dàzhuàng) | 20,162 | 594,729–675,376 |
| 35 | 晉 (Jìn) | 3,336 | 686,433–699,776 |
| 36 | 明夷 (Míngyí) | 3,049 | 699,777–711,972 |
| 37 | 家人 (Jiārén) | 2,838 | 711,973–723,324 |
| 38 | 睽 (Kuí) | 3,843 | 723,325–738,696 |
| 39 | 蹇 (Jiǎn) | 2,520 | 738,697–748,776 |
| 40 | 解 (Jiě) | 3,215 | 748,777–761,636 |
| 41 | 損 (Sǔn) | 4,228 | 761,637–778,548 |
| 42 | 益 (Yì) | 20,602 | 778,549–860,956 |
| 43 | 夬 (Guài) | 4,789 | 875,161–894,316 |
| 44 | 姤 (Gòu) | 3,987 | 894,317–910,264 |
| 45 | 萃 (Cuì) | 4,671 | 910,265–928,948 |
| 46 | 升 (Shēng) | 3,844 | 928,949–944,324 |
| 47 | 困 (Kùn) | 4,942 | 944,325–964,092 |
| 48 | 井 (Jǐng) | 4,164 | 964,093–980,748 |
| 49 | 革 (Gé) | 4,076 | 980,749–997,052 |
| 50 | 鼎 (Dǐng) | 26,928 | 997,053–1,104,764 |

## Files in this deposit

- `iching-dna-full.txt` — the full base stream, wrapped at 60 bases per line.
- `I-CHING-DRAFT-ASSEMBLY-352-OF-450.txt` — the source of record (pure
  concatenation of the seven draft files, tabled above).
- `MANIFEST-DNA-ICHING-DRAFT.md` — this manifest.
- `encode_iching_dna.py` — the encoder (component verification, assembly,
  structure parse + encoding).
- `validate_iching_dna.py` — the hygiene validator (report-only).
- `decode_iching_dna.py` — the separate decoder, written and run by a
  separate agent.
- `INDEPENDENT-DECODER-REPORT.md` — the separate decoder's verdict.
- `ICHING-DNA-DRAFT-PRINT.pdf` — the paper book typeset from the verified
  sequence file: **218 pages**, **637,618 bytes**, SHA-256
  `ba13f8cb9813dc592b9de26df9285dada2bf650f5751efe147b87d24c0c22043` (its printed base stream was re-verified equal to
  `iching-dna-full.txt` IN FULL by extraction of every printed page, and
  three 200-base slices of the extracted stream decode back to the source
  bytes at the corresponding offsets — see the lane's PDF verification
  record).

## Codec hygiene (validator — report only)

- Alphabet: A, C, G, T only — pure.
- Base counts: A 292,896 · C 330,535 · G 307,640 · T 173,693
- GC content: 57.7657%
- Homopolymer runs: 878,687 in total; longest run **8**;
  runs of length ≥ 4: 727 · ≥ 5: 229 · ≥ 6: 30 · ≥ 8: 15 · ≥ 10: 0

The sequence was **not** altered to improve these figures; they are disclosed
for any future synthesis discussion. A synthesis-grade layer would add
screening, addressing, and error correction on top of this codec.

## Separate verification

A separate agent wrote a separate decoder from the specification alone — no encoder or validator code read or shared — and ran it end to end. **VERDICT: PASS.** Its decoded bytes are byte-for-byte equal to the source file and hash to `1a84b3b8b98e6614c738281d44c6da581a9bd38e3a4914e02fd1a5e3be49f225`, the source figure printed above; the base stream hashes to `1b53bbd55814d2db17c117e04d0da911652bda914278087ab818082ed56fe2fd`, also as printed above. Its spot proofs re-encoded the first, middle, and last 1,000 source bytes with its own logic and matched the sequence exactly at each place (1,104,764 bases in total; 276,191 bytes decoded), and each of the seven component slices of its decoded stream hashes to the SHA-256 printed for that component in the table above. Its report, `INDEPENDENT-DECODER-REPORT.md`, is included in this deposit. The printed book's stream was additionally re-verified in full: every Courier span extracted from every page of the PDF, concatenated in order, equals `iching-dna-full.txt` exactly, and three 200-base slices of the extracted stream (start, midpoint, end) decode back to the source bytes at the corresponding offsets.
