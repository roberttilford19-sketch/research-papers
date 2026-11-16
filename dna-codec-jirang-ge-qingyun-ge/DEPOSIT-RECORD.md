# DEPOSIT RECORD — Two Ancient Songs in DNA Letters

**Built 2026-11-15** by the desk, on the commission recorded in `PROJECT-BRIEF.md`. **Status: built and verified locally; NOT shelved — shelving awaits Robert's word.**

## The works and the settled texts

**1. 击壤歌 (Jī Rǎng Gē) — Song of the Earth-Drummers** (primary)
Settled text, as encoded (28 characters):
日出而作，日入而息。凿井而饮，耕田而食。帝力于我何有哉！
English rendering (DeepSeek's): "I work when the sun rises, rest when it sets. I dig my well and drink, plow my field and eat. What is the emperor's power to me?"
Received traditional-character form, for the record: 日出而作，日入而息。鑿井而飲，耕田而食。帝力于我何有哉！

**2. 卿云歌 (Qīng Yún Gē) — Song of the Auspicious Clouds** (companion)
Settled text, as encoded (20 characters):
卿云烂兮，糺缦缦兮。日月光华，旦复旦兮。
English rendering (DeepSeek's): "The auspicious clouds shine brilliantly, intertwined and flowing. The sun and moon radiate splendor—dawn, and dawn again."
Received traditional-character form, for the record: 卿雲爛兮，糺縵縵兮。日月光華，旦復旦兮。

**Character-set note (in the same breath as the build):** DeepSeek settled both texts in simplified characters, and the desk encoded exactly the texts he settled. The wording agrees character-for-character with the received classical texts; only the character set differs (simplified as returned vs. the traditional forms recorded above). If Robert rules the traditional forms should be the encoded edition, the re-encode is a one-step rebuild under the same verification.

## Encoding and verification (house codec)

Codec: UTF-8 bytes → bits → 00=A, 01=C, 10=G, 11=T. Deliberately uncompressed and transparent. This is an **encoding, not a translation**. The deposits are letter sequences only — **no physical DNA exists, and none is made or implied.**

- 击壤歌： 84 bytes → **336 bases**. Source SHA-256: `d9e3ae11aadc58fc19f56b73f0bbb4c2be110b54b79759c15acff4dea018c9cf`. Longest homopolymer run: 4. Sequence file: `jirang-ge-dna.txt`.
- 卿云歌： 60 bytes → **240 bases**. Source SHA-256: `e2e5f46b7fe55ad44c5f7337280ed550ccd9afa06f2160ff2cd6e9a0a00978ac`. Longest homopolymer run: 4. Sequence file: `qingyun-ge-dna.txt`.
- **Round trip: PASS for both** — the desk's decoder (`encode_and_verify.py`, run 2026-11-15) decoded each sequence back to bytes identical to the source and text identical to the settled text.

## Credits

- **DeepSeek (the Green Dragon)** — primary role, named first by Robert's ruling: settled both texts, made both English renderings, led the prior-art search.
- **Awen by Muse by Meta** — the desk: encoding, independent round-trip verification, this deposit.
- **Robert Tilford** — author and publisher; the gift is his to shelve or hold.

## Prior art

DeepSeek's finding, reported 2026-11-15: **none found after research (as of 2026-11-15)** for a machine-verified DNA encoding of either specific poem. This is DeepSeek's search, relayed by Robert; the desk has not independently re-run that search as of this writing, and the claim is carried at that tier. Firstness, if ever stated publicly, attaches only to the published, machine-verified DNA-letter encoding of this edition, in the house wording "none found after research," dated.

## Provenance of the return

DeepSeek's return (settled texts, renderings, prior-art findings) reached the desk as a screenshot relayed by Robert on 2026-11-15 (~16:57 CST) from the "Parallel Desk: The Poem Deposit" conversation. The settled texts were transcribed from that screenshot character by character and cross-checked against the received classical texts before encoding.

## Terms

© Robert Tilford — given free, never sold; attribution requested.

---
**Addendum — traditional characters (2026-11-15, Robert's ruling, tap A):** The deposit's face is the traditional text, per the brief. Re-encoded and re-verified at the desk the same evening: 擊壤歌 — 日出而作，日入而息。鑿井而飲，耕田而食。帝力于我何有哉！— 28 characters, 84 bytes, 336 bases, source SHA-256 3ccf8b878346bfac948fa08c1c0dee1724f314e1b50fe7049473c66cbedfb023, round-trip PASS, longest homopolymer run 4. 卿雲歌 — 卿雲爛兮，糺縵縵兮。日月光華，旦復旦兮。— 20 characters, 60 bytes, 240 bases, source SHA-256 54b933573bac4eab7707c7f6156f214eb5c7f8f749e63e895500acddff2b2fca, round-trip PASS, longest homopolymer run 4. The simplified texts exactly as DeepSeek returned them are preserved in this folder (files marked SIMPLIFIED-as-returned, texts and DNA), superseded as the deposit's face, not erased. DeepSeek's credit is unchanged.

---
**Shelving addendum (2026-11-15, Robert's ruling — Decision 4, tap A):** Shelved the same evening to roberttilford19-sketch/research-papers (branch main), folder `dna-codec-jirang-ge-qingyun-ge/`, by Git Data API on the then-current HEAD, following the pattern of the Constitution and Magna Carta lanes. Landed files: this record, `PROJECT-BRIEF.md`, the traditional source texts and DNA sequences, `encode_and_verify.py`, and the four SIMPLIFIED-as-returned preservation files. `INVITATION-TO-DEEPSEEK.txt` stays home, per the pattern lanes (deposits carry no correspondence). The commit hash is recorded in the desk's shelving report and day log; a record cannot carry its own commit hash.
