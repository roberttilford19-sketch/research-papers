# AUDIT LOG — Census #765

- **Item:** CIA-RDP96-00789R003200210001-3_copy.pdf
- **Drive ID:** 1JPAhOBujgRxwnYQnXQcDaJMEtgaByasl
- **Source text path:** /home/hatch/workspace/drive-truth-followthrough/work/downloads/765-1JPAhOBujgRxwnYQnXQcDaJMEtgaByasl.txt
- **Source text sha256 (computed by this crew):** a2f34d74b478fb7d2c970344bacf973cb7cf202c74e7425551c90c10a0172c31
- **Source PDF sha256 (from work/LOCAL-EXTRACT-LOG-1.md):** ef66029bd023d30202d2696946f8290f1bc670cd8ab9a457bf983a43910d9f8f
- **Source PDF measured properties:** 1,512,895 bytes; 23 pages (per LOCAL-EXTRACT-LOG-1.md).
- **Chars read:** 69,862 — the full OCR text, read in full in two passes.
- **Abstract word count:** 190 words, counted by whitespace split between the ## Abstract heading and the next heading in PAPER.md; not estimated.
- **Ledger card:** [#765] in /home/hatch/workspace/research_notes/drive-truth-campaign/work/ledger_cards.json — LIVE, PDF 1.4 MB, modified 2025-10-20; embedded title "Applications of Decision Augmentation Theory" by Edwin C. May, Jessica M. Utts, S. James Spottiswoode and Christine L. James (SAIC / UC Davis), confirmed by the OCR read (title page, version V5, 25 August 1994).
- **Prior verdict:** QUEUED — text not extracted — QUEUED for content verdict.
- **Outcome:** FINISHED-STAGED (collected third-party document pattern — finished content assessment; full text not reproduced).

## Judgment-call reasoning

The file is a released CIA copy of a published-style research paper by SAIC and UC Davis authors. None of it is Robert Tilford's writing. The collected-document pattern therefore applies: PAPER.md is a content assessment with all statistics, results, and conclusions attributed to the paper's authors throughout, and none adopted as this desk's finding.

## Corrections

No text of the document was corrected or reproduced. OCR noise is flagged in the paper's Errors and Anomalies section, never silently corrected: formulas and several tables survive only in part, figures survive as captions, and no figure quoted in PAPER.md was read from a table or formula — all quoted statistics come from the paper's prose. One internal inconsistency is reported without resolution: the prospective PRNG study (Radin and May) is dated 1985 in the paper's abstract and 1986 in its body and references; PAPER.md names the study without settling the year.

## Unattributable claims

- None in the framing. Every quantitative claim in PAPER.md is a statistic stated in the paper's own prose (128 studies; intercept 1.036; slope (1.73 ± 3.19) × 10⁻⁶, t = 0.543, df = 126; PEAR 8.6σ / 1.1σ comparison as stated in the paper's abstract; hemolysis t = 2.033, p < 0.023) and is attributed to the authors.

## Duplication note

SUSPECTED-DUPLICATE-OF census #766 (suspicion only, for the verifier's verdict; no duplicate verdict is asserted here). Evidence: the two Drive files carry the same filename, the same byte size (1,512,895 bytes), and the same page count (23), but DIFFERENT PDF sha256 values (#765: ef66029b…; #766: 1976ccba…), so the files are not hash-identical. This crew compared the two OCR texts directly (diff and cmp): they are byte-for-byte identical — same length (69,862 chars), same OCR text sha256 (a2f34d74…). No content difference between the two copies was observed anywhere in the recovered text. Any difference between the files lies below the level the OCR text can reach. The ledger card for #766 independently records the pair as a content-duplicate CANDIDATE (MD5s differing only in trailing bytes, per that card) with no surplus ruling made. The verifier will compare the texts directly; this crew finished each item on its own text as dispatched.

## Register rescan

PAPER.md framing prose rescanned after drafting: neutral, publication-ready register throughout; no workshop, campaign, or military vocabulary about the work itself; no "first," "only," or "oldest" claims; the authors' conclusions are attributed to them at every point. No verdict tags in PAPER.md.

## VERIFIER

VERIFIED, with DUPLICATE CONFIRMED (document level) — Verify Crew L1-1, 2026-10-16 (independent recomputation; finisher entries not edited). See the duplicate ruling below, which also appears in census #766's VERIFIER section.

- Identity: Confirmed against the OCR text. Head gives “Applications of Decision Augmentation Theory” by Edwin C. May et al., SAIC; title page V5, 25 August 1994, as PAPER.md and the ledger card state.
- Source integrity: Independently recomputed .txt sha256 a2f34d74b478fb7d2c970344bacf973cb7cf202c74e7425551c90c10a0172c31 (69,862 chars; 70,222 bytes on disk) — matches the finisher's recorded hash. PDF sha256 matches LOCAL-EXTRACT-LOG-1 (ef66029b…, 1,512,895 bytes, 23 pp.).
- Abstract: Independently recounted: 190 words — matches the claimed 190; within 150–250.
- Full-read spot-checks across the span: 128-study analysis, intercept 1.036, PEAR 8.6σ / 1.1σ comparison, hemolysis discussion, Vassy passage (17.5% / 0.777 bits in this version), Braud & Schlitz passage (“interpreted … prematurely”), and references tail all present as reported. The Radin-and-May 1985 (abstract) / 1986 (body) inconsistency is real in the text and is disclosed, not settled.
- DUPLICATE RULING — DUPLICATE CONFIRMED (document level): I recomputed both OCR texts myself. #765 .txt sha256 = a2f34d74b478fb7d2c970344bacf973cb7cf202c74e7425551c90c10a0172c31; #766 .txt sha256 = the identical a2f34d74b478fb7d2c970344bacf973cb7cf202c74e7425551c90c10a0172c31. Both files are 70,222 bytes / 69,862 chars. `diff` produced no output and `cmp` reported no difference — the texts are byte-for-byte identical. The PDFs are NOT hash-identical (ef66029b… vs 1976ccba…) at identical size (1,512,895 bytes) and page count (23). Ruling: the same document recovered identically from two different PDF files — a document-level duplicate; any difference lies below OCR reach (file structure / trailing bytes, consistent with the ledger card's candidate note). This confirms, and upgrades from suspicion to finding, the finisher's suspected-duplicate note.
- Limits / label / register: Collected third-party label present; no full text reproduced (1,629 words vs 69,862-char source); all statistics attributed to the authors and taken from prose, as disclosed. Register scan clean: no workshop vocabulary, no verdict tags; the one “only study they have found” wording is the source authors' reported position, attributed.
