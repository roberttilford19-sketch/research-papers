# Audit Log — Census 1401

## Source

- **Source text path:** /home/hatch/workspace/drive-truth-followthrough/work/downloads/1401-1kLTQLrZ2f32-F2dO_MJD69ngJiib6NHX.txt
- **SHA-256 of source text (computed by this crew with sha256sum):** f33b3c807a69e4cd58a383531e1ce40321675e2b5777cd831d89bb194198796c
- **SHA-256 recorded in LOCAL-EXTRACT-LOG-2.md for this item:** 3a516b221ba2c6d83f0b90b431aef4671dac60c6e5d33a8a4d1513b585c4231e (the extract log's hash is recorded against the recovered PDF binary; the text-file hash above was computed separately by this crew and the two are not expected to match, since they hash different files).
- **Source text size:** 4,887 characters per the extract log; 4,948 bytes on disk.
- **Chars read:** 4,887 of 4,887 — the full OCR text on disk was read. No sampling.
- **Underlying PDF:** 2 pages (extract log).

## Ledger card and prior verdict

- **Ledger card:** [#1401] in TRUTH-LEDGER.md (line 11308) and in ledger_cards.json.
- **Card facts used:** PDF, 149.5 KB, modified 2024-02-15, LIVE, path <shared/root?>/Grillflame Sci Eval Comm; identified from PDF metadata/filename as "COMMENTS ON 'REPORT BY: THE GRILLFLAME SCIENTIFIC EVALUATION COMMITTEE'," 2 pp.
- **Prior verdict:** QUEUED — text not extracted; needs OCR/content pass before any keep/junk ruling.

## Judgment call — whose document is it?

**Collected third-party document.** Reasoning: the text is a U.S. government memorandum for the record from Dr. J. Verona, Chairman of the Grill Flame Working Group, released under CIA-RDP96-00788R001300060001-2. It contains no writing by Robert Tilford. PAPER.md is therefore a finished content assessment with the honest collected-document label, and the full text is NOT reproduced, per the brief.

## Known relation (recorded per dispatch instruction)

- **Related item, not a duplicate:** census [#1153], the Grill Flame Scientific Evaluation Committee report itself, finished and verified separately and staged at `staged/1153-grill-flame-scientific-eval/`. This item is a two-page commentary on that report by the chairman of the working group whose programme the committee reviewed. The relation is recorded in PAPER.md's Identification block and in this log. The 1153 audit log independently records the same relationship from the other side.

## Corrections made (staged copy only; originals unaltered)

Because the collected-document pattern does not reproduce the source text, there are no in-text corrections to the document itself. Readings and normalisations in this crew's own framing, each with its basis:

1. **Author and role normalised** from the garbled OCR header to "Dr. J. Verona, Chairman, Grill Flame Working Group." Basis: the memorandum's signature block and subject line as OCR'd, which are legible in substance.
2. **Identification of the two Army activities in the garbled disagreement passage.** The OCR at that point is partly unreadable. PAPER.md identifies the activities as the Army Missile Intelligence Command's psychokinesis investigations and the Material Systems Analysis Activity's remote viewing investigations, and states openly that this identification follows the committee report at census 1153, whose recommendations name those activities, rather than a clean reading of this scan. Basis: cross-check against the finished 1153 assessment; flagged in PAPER.md's Errors and Anomalies section, not silently settled.
3. **The memorandum's date is NOT asserted.** No date is legible in the recognized text, and none appears in PAPER.md. Basis: absence in the source text.
4. **OCR noise treated as an anomaly class throughout**, never as errors of the memorandum, and never silently corrected in substance.

## Factual claims that could not be attributed or verified

- All substantive claims in PAPER.md are attributed to the memorandum itself, to ledger card [#1401], or, where expressly flagged, to the census 1153 report. No claim was adopted as this desk's own finding.
- The memorandum's characterizations of the committee report ("serious factual errors," "an inordinate number of ambiguities," incomplete and narrowly focused) are the Working Group's position as an interested party. PAPER.md attributes them to the Working Group and notes that the committee report states its findings in its own terms; the conflict between the two documents is reported, not resolved.
- No "first," "only," or "oldest" claim is made anywhere in PAPER.md. The memorandum's phrase "this first attempt at a comprehensive evaluation" is the document's own wording, quoted in substance as its closing sentiment and not adopted as a primacy claim by this desk.

## Duplication note

- **Not a duplicate of census 1153 or of any other item.** A two-page commentary on a 94-page report is a distinct document. The relationship is recorded above and in PAPER.md; no SUSPECTED-DUPLICATE-OF verdict is asserted.

## Register rescan

PAPER.md was rescanned after drafting for workshop, campaign, and military vocabulary about the work itself. None was found. References to the Army, the intelligence community, and named Army activities refer to the historical institutions that are the document's subject. The framing prose is neutral, in full sentences, with the memorandum's claims attributed to it throughout.

## Abstract check

The abstract in PAPER.md is 221 words (counted programmatically by this crew on a whitespace split), within the brief's 150–250 word requirement, and was written from the full text actually read.

## VERIFIER

**VERIFIED — VERIFY CREW L2-6 (independent), 2026-10-16. Full log: work/VERIFY-LOG-L2-6.md.**

- Identity re-derived from the OCR text: "MEMORANDUM FOR THE RECORD," "FROM: Dr. J. Verona, Chairman, GRILLFLAME Working Group," subject "Comments on 'Report By: The GRILLFLAME Scientific Evaluation Committee'," release stamp CIA-RDP96-00788R001300060001-2 — as PAPER.md states. No date is legible in the OCR and none is asserted. Source-text sha256 recomputed: f33b3c807a69e4cd58a383531e1ce40321675e2b5777cd831d89bb194198796c, matching this log; 4,887 chars, full read as claimed.
- Abstract independently recounted at **221 words** (finisher: 221), within 150–250.
- Content spot-checks match the OCR: the opening objection ("serious factual errors, an inordinate number of ambiguities, is incomplete and narrowly focused," danger of "arbitrary guidance to policy makers and planners"); both points of support, including the Working Group's own "intrinsically non-scientific" note; the recommendations (expanded exploratory testing in the order utility, existence, characterization; a central authority to manage and fund; continued foreign intelligence analysis); and the closing offer with the collectively-reviewed-in-draft regret.
- Relation to #1153 (special a) — CONFIRMED, related not duplicate: I read the staged #1153 paper (`staged/1153-grill-flame-scientific-eval/PAPER.md`) in full. It assesses the December 1979 Grill Flame Scientific Evaluation Committee report (94 pp., CIA-RDP96-00788R001300120001-5), whose recommendations were that "the remote viewing work at AMSAA and the psychokinesis experiments at MICOM, together with their supporting contracts at SRI, should be discontinued." This two-page Verona memorandum is a commentary responding to that report — a distinct, much shorter document answering it, not a copy of it. PAPER.md states the relation exactly that way in its Identification block.
- Garbled-passage flag (special a) — CONFIRMED: PAPER.md's disagreement section and Errors and Anomalies section both state openly that the scanned text is badly garbled at the Army-activities passage and that the identification (Army Missile Intelligence Command psychokinesis investigations; Material Systems Analysis Activity remote viewing investigations) follows the committee report at census 1153 rather than a clean reading of this scan. That flag is accurate and conservative: the OCR at that passage is partly legible in garbled form ("terminate the Army's Missile Intelligence Command's PK and Material Systems Analysis Activitic's RV investigations… based on a misinterpretation") and is fully consistent with #1153's AMSAA/MICOM/SRI termination recommendation, which the verifier confirmed independently in #1153's paper. The SRI passage likewise names Puthoff and Targ in the OCR in garbled form. No unflagged claim rests on a garbled passage.
- Collected-document label and honest label present; no full text reproduced (shared 12-word shingles: 32, all single quoted sentences of the memorandum — its objection, its central-authority recommendation, and its closing passage — quoted inside a longer original assessment).
- Register scan (independent): clean; the memorandum's own "first attempt at a comprehensive evaluation" wording is reported as the document's, not adopted as a primacy claim.
