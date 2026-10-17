# AUDIT LOG — Census #142

## Source

- Drive filename: DOW-UAP-D086_USNavy-Report-of-Flying-Discs_1948.pdf
- Drive ID: 1ctDOKbZmIGGq9YUg8xN2hHh_hONMSq34
- Source text path: /home/hatch/workspace/drive-truth-followthrough/work/downloads/142-1ctDOKbZmIGGq9YUg8xN2hHh_hONMSq34.txt
- Source PDF path (beside the text, same stem): /home/hatch/workspace/drive-truth-followthrough/work/downloads/142-1ctDOKbZmIGGq9YUg8xN2hHh_hONMSq34.pdf
- sha256 of the source text (.txt): 379b8e69355a0c4e3b59f42b046eb9b97ea6c13e6fd4c8954145295ea2a870f1
- sha256 of the source PDF: f96457d53f3cd65aec3fc539e7138cc42a5ea962654a83c75abbd0f13d54383c
- PDF facts (pdfinfo): 3 pages; 4,486,402 bytes; PDF 1.7; producer "Adobe Acrobat (32-bit) 26 Paper Capture Plug-in"; permissions print yes, copy no.
- Ledger card: [#142] in TRUTH-LEDGER.md and ledger_cards.json. Prior verdict: QUEUED — "text not extracted — QUEUED for content verdict." Card state: LIVE, 4.3 MB, modified 2026-06-23.

## Extraction measurement and OCR method (per coordinator steer)

- The extracted text on disk measures 59 bytes. FETCH CREW 1's formal report measures the extractable content text at 56 characters across 3 pages. Direct re-extraction with pdftotext in this session reproduced the same 59-byte file. The PDF is effectively a scan with no usable text layer; the only legible extracted fragment is the declassification line "Authority: NND 740185."
- Per the coordinator steer, the item was worked from the PDF itself, locally, with no connector. Pages were rendered with PyMuPDF at 250 dpi (pdftoppm at 300 dpi stalled in this session after rendering two pages and was terminated; the PyMuPDF renders of all three pages were used). Renders were converted to grayscale and downscaled by a factor of 0.8 (approximately 200 dpi effective) for recognition.
- OCR engine: tesseract, language eng, primary configuration --psm 3. Primary OCR output, saved in the staged folder as OCR-EXTRACT-psm3.txt: page 1 = 73 characters, page 2 = 1,811 characters, page 3 = 128 characters; total 2,012 characters, 371 words.
- Other configurations tried, for the record: --psm 1 at 250 dpi on the colour renders gave page 1 = 106 characters (recovering "1948," "DATE CLOSED," "Office, Chief Army Field Forces," "A. G. Files") and 0 characters on pages 2 and 3. --psm 6 on hard-thresholded (binarized at grey level 180) images degraded the text badly and was not used. --psm 4 and --psm 11 on page 2 gave character counts comparable to --psm 3 (1,825 and 1,870) with no additional reliable content.
- Character counts read for this finish: extracted text 56 characters (content); OCR primary run 2,012 characters across all 3 pages (100% of pages OCR'd; no sampling). Page-level readability: page 2 substantive and largely clean in its operative paragraphs; page 1 partial; page 3 fragments only.

## Judgment call — whose document is it?

Collected third-party document. The file is a declassified 1948 United States government record (Fifth Naval District correspondence quoting a Chief of Naval Operations letter, filed in an Office, Chief of Army Field Forces Adjutant General file). Nothing in it is Robert Tilford's writing. PAPER.md is therefore a finished content assessment with the honest collected-document label, and the full text is not reproduced.

## Corrections (framing normalizations, staged copy only; originals unaltered)

All corrections are normalizations of OCR output in this crew's own framing prose. No words of the document are quoted as verbatim where OCR was uncertain. Each rests on internal consistency within the OCR output itself:

1. "Flying Dises" / "Flying Discs" variants in the subject line and body normalized to "Flying Discs." Basis: the word is rendered correctly as "Discs" multiple times in the same OCR output, and the Drive filename carries "Flying-Discs."
2. "Fifth Naval Distfict" normalized to "Fifth Naval District." Basis: "District" is rendered correctly repeatedly in the same page's OCR.
3. "13 Deo 19/8" normalized to "13 December 1948." Basis: the cover page OCR and the filename both give 1948; "Deo" follows the standard date-line pattern and December is the only month reading consistent with the characters; flagged here as a normalization, not a verbatim read.
4. "phenomene be investigatad," "unidentified serial objects," "photogrephic evidence," "by the festest moans," and similar garbles in the operative paragraphs were paraphrased in clean prose rather than quoted. Basis: the surrounding sentences are complete and unambiguous in the OCR output; no meaning was added.
5. "A. G. Files" on the cover was expanded once in the content account as "Adjutant General file." Basis: standard U.S. Army usage of the abbreviation A.G. for Adjutant General on a file cover of this office; the unexpanded form is retained in the abstract and identification so the expansion is visible as an interpretation.
6. Reference (a)'s serial number and exact date were NOT normalized or stated. The OCR reads them garbled ("Serial ol22P32, dtd November 19," in one run) and no internal control exists; they are logged as unresolved in the paper's LIMITS.

## Unattributable claims

- The quoted Chief of Naval Operations letter's assertion that "a cycle of reappearance of 'Flying Discs' is becoming apparent" and that "the beginning of a new interval is imminent" is the document's own claim, relayed from the Director of Intelligence, U.S. Air Force. It is attributed to the document in PAPER.md and not adopted.
- The letter's statement that the Air Force requested quick reporting and investigation is likewise attributed to the document.
- No sighting, witness, location, or physical evidence is described anywhere in the recovered text; none is claimed.
- The filename's series label "DOW-UAP-D086" and the "Department of War release series" framing come from the Drive filename and the ledger card, not from the document's own pages.

## Duplication note

No suspected duplicate. The ledger was searched for "D086," "Fifth Naval," "Inglis," and "Flying Discs"; the only match is census #142 itself. Neighbouring items in the same release series (for example #141, DOW-UAP-D084, a 1949 U.S. Army flying-saucer study) are different documents by filename, service, and year. No SUSPECTED-DUPLICATE-OF verdict is entered; any duplication ruling belongs to verification.

## Register rescan

PAPER.md was rescanned after drafting. It contains no crowns (no "first," "only," or "oldest" claims), no workshop or campaign vocabulary in the framing prose, and no ledger shorthand. Military and naval terms that appear (Naval District, Chief of Naval Operations, district intelligence officer) are the document's own subject matter, not framing. All factual statements in the framing are attributable to the OCR output, the embedded text layer, pdfinfo metadata, the Drive filename, or the ledger card, as logged above.

## Files staged

- PAPER.md — finished content assessment (collected-document pattern).
- AUDIT-LOG.md — this log.
- OCR-EXTRACT-psm3.txt — the primary OCR output (tesseract --psm 3, all three pages concatenated), retained as supporting evidence for verification. Intermediate renders remain in /tmp/142ocr/ (ephemeral).

## VERIFIER

**VERIFY CREW 12 — 2026-10-16 — VERDICT: VERIFIED, with precision notes (below; not counted as a discrepancy).**

Independent recomputation and spot-checks; PAPER.md not edited; staging only; no connector use; originals unaltered.

- **Hashes — exact match.** Source PDF sha256 recomputed `f96457d53f3cd65aec3fc539e7138cc42a5ea962654a83c75abbd0f13d54383c`; source .txt sha256 recomputed `379b8e69355a0c4e3b59f42b046eb9b97ea6c13e6fd4c8954145295ea2a870f1`. Both match this log. pdfinfo independently confirms 3 pages, 4,486,402 bytes, PDF 1.7, producer "Adobe Acrobat (32-bit) 26 Paper Capture Plug-in," print yes / copy no.
- **Extracted layer — confirmed.** The .txt is 59 bytes decoding to exactly 56 characters. Its only legible fragment is "Authority: NND 740185."; the remainder is whitespace, form feeds, and two stray glyphs ("•", "£") plus the fragment "f: F." — no other legible words.
- **Abstract — confirmed.** Independently recounted at **225 words** (whitespace split), matching the claim and within the 150–250 requirement.
- **Content spot-checks against the staged OCR — pass.** Page 1: "DATE CLOSED," "Office, Chief / Army Field Forces," "A. G Files" all present in the psm 3 extract. Page 2: Headquarters, Fifth Naval District, Norfolk 11, Virginia; Commandant to activities in the distribution list; subject "'Flying Discs' — Report of"; the quoted Chief of Naval Operations letter's cycle-of-reappearance passage; the directions to report to the nearest Air Force command and the Naval District Intelligence Office, to obtain photographic evidence whenever possible, and for district intelligence officers to forward to the Chief of Naval Intelligence for passage to the Director of Intelligence, U.S. Air Force, by the fastest means; signatures Thos. B. Inglis ("By direction") and R. C. Hudson, Chief of Staff — all findable in the OCR text. Page 3: "DISTRIBUTION CENTER" and a "DEC" date fragment present; the rest is fragments only, as the paper states.
- **Attribution and limits — confirmed.** The "cycle of reappearance" assertion is attributed to the document / the quoted letter in the abstract, the content account, and the closing separation paragraph, and is nowhere adopted as the paper's own finding. The reference letter's serial number and exact day-date appear nowhere in PAPER.md (the paper states only "November 1948," which the OCR supports, and expressly declines to state the garbled serial and exact date); the garbled OCR reading printed in this log's Corrections §6 is presented there only as an unresolved example, not as a statement in the paper. The LIMITS section states page 3's fragmentary yield plainly, including that any content unique to page 3 is not represented.
- **Label and register — confirmed.** The collected third-party document label is honest (1948 U.S. government file; expressly not Robert Tilford's writing). Independent rescan of PAPER.md finds no campaign or workshop register and no crown claims; "first" occurs only as "first page" and "only" only as a limiting qualifier; naval and Army terms are the document's own subject matter.

**Precision notes (recorded, not counted as a discrepancy):**

1. The OCR counts in this log are byte counts labelled as characters. The staged OCR file is 2,012 **bytes** and 1,983 **characters** (UTF-8 codepoints). The claimed per-page split reconciles exactly in bytes — page 1: 73 bytes / 73 characters; page 2: 1,811 bytes / 1,787 characters; page 3: 128 bytes / 123 characters — so the evidence file and its split are intact and reproducible; only the unit label is imprecise for pages 2–3 and the total.
2. The log's "371 words" for the OCR output does not reproduce: the staged file counts **377 words** by both whitespace split and `wc -w`. No claim in PAPER.md rests on this figure.
3. Two paper details rest on the finisher's logged supplementary runs rather than on the staged psm 3 extract alone: the cover year "1948" (recovered in the logged --psm 1 run, not present in the psm 3 page-1 text) and the distribution-list enumeration "1A, 2A, 3A, 6A, 7A, and an 85-copy entry" (only 1A, 3A, and 6A are legible as such in the psm 3 extract; the paper itself hedges that the list was recovered only in part). Both are disclosed in method terms in this log; neither affects the paper's substantive account.
