# Audit Log — Census 1405

- Source text path: /home/hatch/workspace/drive-truth-followthrough/work/downloads/1405-1lCkHPGaJ3pj8-S4rJrCVxMssgX9QBPEO.txt
- Source text sha256 (computed at this desk from the .txt file): 243e1b571de6637ef9c5fa4ea1d1df4793dfb961605948d5625e44b581cb5485
- PDF binary sha256 (from LOCAL-EXTRACT-LOG-2.md): 23f02aa2d29896fdf04a527fcb7a802ee356f32e24a24c64101f4747979ae83f; 6,809,237 bytes; 118 pages; OCR-CAPPED at 60 pages.
- Text length: 84,364 characters per the extract log; 84,364 characters in the file as read (84,710 bytes on disk including encoding overhead).
- Ledger card prior verdict: QUEUED — text not extracted; identified from metadata only as ADVANCED THREAT TECHNIQUE ASSESSMENT, SRI Project 5309, 118 pp. Ledger card source: TRUTH-LEDGER.md, entry [#1405]. The ledger_cards.json copy consulted did not contain an entry under this census number; the TRUTH-LEDGER.md entry was used.
- Judgment call: Collected third-party document. The text carries SRI International authorship (Puthoff, Targ, May, Swann), a DIA classification history, and a CIA release stamp. It is not Robert Tilford's writing, so PAPER.md is a content assessment and the full text is not reproduced.
- Reading: Title pages, contents, and illustrations list read in full. The submersible protocol section and the closing feedback discussion read in full. Other chapters sampled at the opening, quarter, and midpoint positions. Figure-heavy sampled pages yielded garbled recognition output and were treated as unassessed images.
- Corrections: None. Collected-document pattern: no staged copy of the text is produced, so no corrections were applied. OCR noise was flagged as an anomaly class in PAPER.md and was never silently corrected or treated as substance.
- Unattributable claims: All experimental results reported in PAPER.md are attributed to the report's authors. The document's claims about remote-viewing accuracy, the submarine communication example, and the importance of feedback are the authors' claims; this desk ran no independent verification and adopted none of them.
- Duplication: No duplicate suspected within this assignment set. An initial sampling artifact briefly suggested Grill Flame question-and-answer text in this file's tail; a direct search of the full text found zero occurrences of "GRILL" in this file, and the actual tail is the feedback chapter. That suspicion is recorded here as checked and not sustained. Item 1416 in this set is a separate Grill Flame document with its own file and hash.
- Register rescan: PAPER.md framing was rescanned after drafting. It uses neutral descriptive language, attributes all claims, and contains no superlative or primacy claims and no workshop vocabulary.
- Staging only: Nothing published, pushed, emailed, posted, uploaded, or deleted. The source text and Drive original were not altered.

## VERIFIER

- **VERIFY CREW L2-7, 2026-10-16: DISCREPANCY — scoped to the ledger-source statement only; every content check below passes.** The finisher statement that "the ledger_cards.json copy consulted did not contain an entry under this census number" is not sustained. At `~/workspace/research_notes/drive-truth-campaign/work/ledger_cards.json`, the `cards` dict does contain key `"1405"`, and its text is exactly identical (657 characters) to the `[#1405]` entry in `TRUTH-LEDGER.md`. Both sources hold the card, with the same QUEUED prior verdict and the same identification (ADVANCED THREAT TECHNIQUE ASSESSMENT, SRI Project 5309, 118 pp.). The content assessment is unaffected, but the source statement must stand corrected by this verifier addendum.
- Identity vs OCR: VERIFIED. My recomputed sha256 of the OCR text is 243e1b571de6637ef9c5fa4ea1d1df4793dfb961605948d5625e44b581cb5485 (84,364 characters / 84,710 bytes), matching this log. The OCR head reads Final Report October 1978, ADVANCED THREAT TECHNIQUE ASSESSMENT, by Harold E. Puthoff, Russell Targ, Edwin C. May, and Ingo Swann, covering 18 April 1977 to 18 April 1978, SRI Project 5309 — exactly the PAPER.md identification. Taurus / Santa Catalina / submersible material is present in the text as the paper describes.
- Abstract: independently recounted at 230 words (required 150–250; within the finisher's claimed 223–243 set range).
- Cap statement: VERIFIED exact in substance in Limits — "The source PDF has 118 pages. Only the first 60 pages were converted" and "No claim in this assessment rests on pages 61 to 118."
- Grill Flame suspicion: VERIFIED checked-and-not-sustained. My own case-insensitive full-text search of the OCR text returns zero occurrences of "GRILL" and zero of "grill flame"; the file tail is the feedback / digit-guessing chapter, ending at the page-59 marker, as the finisher recorded.
- Collected-document label: present in PAPER.md Identification ("Collected third-party document … not a document by Robert Tilford"), with "not reproduced" stated. No full text reproduced: PAPER.md is 963 words against an 84,364-character source; 12-word verbatim shingle overlap is only 2 shingles, both in the single Taurus identification phrase.
- Register scan: no workshop vocabulary, no primacy / superlative claims found.


## ADDENDUM — 2026-10-16 — REPAIR CREW L2-7

This addendum is appended on 2026-10-16. It does not edit, delete, or replace any existing finisher or verifier entry in this log. It corrects one ledger-source statement only, and it leaves the content assessment in PAPER.md unaffected.

The incorrect statement, in the finisher's entry above, is: "The ledger_cards.json copy consulted did not contain an entry under this census number; the TRUTH-LEDGER.md entry was used."

The corrected fact, verified at this desk on 2026-10-16, is that both sources hold the card for census 1405. The file at ~/workspace/research_notes/drive-truth-campaign/work/ledger_cards.json is a dictionary with a "cards" key keyed by census number as strings, and it does contain an entry under the key "1405". The file at ~/workspace/research_notes/drive-truth-campaign/TRUTH-LEDGER.md also contains the entry headed "### [#1405] Remote Viewing, Long Distance, Sub". The text of the ledger_cards.json entry and the text of the TRUTH-LEDGER.md entry, stripped of the trailing blank lines that separate entries in the Markdown file, are identical, and each measures 657 characters. The card substance therefore agrees in both sources, including the QUEUED prior verdict and the identification as ADVANCED THREAT TECHNIQUE ASSESSMENT, SRI Project 5309, 118 pages.

The basis for this correction is VERIFY CREW L2-7 and its log at ~/workspace/drive-truth-followthrough/work/VERIFY-LOG-L2-7.md, in its ledger-source finding and in its entry for census 1405, which recorded the same discrepancy and the same 657-character identity.

PAPER.md is unchanged by this repair. Its sha256 recorded before this addendum was appended is 90fdf17a1f211d145a3c5c956cf595850c24ea33d9b91f2f6db9de8526b23e9b, and its sha256 after this addendum is recorded by the repair crew's verification check in its report to the coordinator; the repair itself did not open, edit, or write PAPER.md.

Post-append verification, 2026-10-16, REPAIR CREW L2-7: PAPER.md sha256 after this addendum is 90fdf17a1f211d145a3c5c956cf595850c24ea33d9b91f2f6db9de8526b23e9b — identical to the before hash recorded above. PAPER.md is unchanged.
