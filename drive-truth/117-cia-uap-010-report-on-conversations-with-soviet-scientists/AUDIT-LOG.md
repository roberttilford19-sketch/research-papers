# Audit Log — Census #117

## Source

- Census number: 117
- Drive filename: CIA-UAP-010_REPORT_ON_CONVERSATIONS_WITH_SOVIET_SCIENTISTS_ON_SUBJECT_OF_UNIDENTIFIED_FLYING_OBJECTS_IS_THE_USSR.pdf
- Drive ID: 1IAUmAsfe_rcBSMt9o1G9AsEXiffhqLYl
- Document type: PDF
- Size (worklist): 1,673,880 bytes
- Status: LIVE (not trashed)
- Source extract path: /home/hatch/workspace/research_notes/drive-truth-campaign/work/pdf/1IAUmAsfe_rcBSMt9o1G9AsEXiffhqLYl.txt
- Source extract SHA-256: 7060584c3e59f0b2f12f34aa0b40faadf4aa5790a0459f3319852bcd63262cbb
- Extract size: 2 bytes
- Characters read: 2 (both characters read in full; both are form-feed characters, U+000C)

## Prior verdict

- Ledger card [#117] in /home/hatch/workspace/research_notes/drive-truth-campaign/TRUTH-LEDGER.md: "QUEUED — text not extracted — QUEUED for content verdict."
- Ledger card basis, as stated on the card: binary present but extraction empty (2 bytes); card written from filename and embedded PDF metadata only; described on the card as a scanned document whose text layer did not extract.
- Worklist row (QUEUE-WORKLIST.json): census 117, ledger_verdict "QUEUED — text not extracted — QUEUED for content verdict.", status PENDING at the time this staging began.

## Checks performed

1. Read ledger card [#117] in full from TRUTH-LEDGER.md.
2. Read the worklist row for census 117 from QUEUE-WORKLIST.json and confirmed the Drive ID, filename, size, LIVE status, and extract path match the assignment.
3. Measured the extract with a byte count and a character count. Both returned 2.
4. Computed the SHA-256 of the extract, recorded above.
5. Inspected the extract byte by byte. It contains two form-feed characters and nothing else. No words, digits, or punctuation are present.
6. Checked the extract against the requirement for a finished paper: an abstract of 150 to 250 words and a content account must be written from text actually read. The extract contains no readable text, so that requirement cannot be met honestly.

## Corrections and judgment calls

- Judgment call: staged a GAP-NOTE.md instead of a PAPER.md. Basis: the campaign instruction for this treatment states that if an extract is too fragmentary to support an honest abstract, the crew must not pad and must stage a gap note instead. A 2-character extract with zero readable words meets that condition.
- Judgment call: no subject description beyond the filename was asserted as document content. Basis: the ledger card itself states that its summary was written from the filename and embedded metadata only, so the subject wording is attributed to the filename and to the ledger card, not to the document's text.
- Judgment call: no errors-and-anomalies finding was recorded for the document itself. Basis: with no body text read, neither "none spotted" nor any specific anomaly can be stated honestly about the document's contents. The anomaly recorded here concerns the extraction, not the document: a 1,673,880-byte PDF yielded a 2-byte text extract.
- No corrections were made to the original PDF, to the extract, or to the ledger card. All work product is in this staging folder only.

## Outcome

- GAP-NOTE staged. No PAPER.md was created for this item.

## VERIFIER

- Verifier name/crew: VERIFY CREW 1 (Drive Queued-695 Finishing Campaign, independent checker)
- Date: 2026-10-16
- Checks performed:
  1. Recomputed the source extract at /home/hatch/workspace/research_notes/drive-truth-campaign/work/pdf/1IAUmAsfe_rcBSMt9o1G9AsEXiffhqLYl.txt independently: byte size 2, SHA-256 7060584c3e59f0b2f12f34aa0b40faadf4aa5790a0459f3319852bcd63262cbb. Both match the values recorded in this log exactly.
  2. Read the extract byte by byte: it is exactly two form-feed characters (U+000C, U+000C) and nothing else — no words, digits, or punctuation. The GAP-NOTE's content description is accurate; no read of document body text is claimed anywhere in the package.
  3. Read ledger card [#117] in /home/hatch/workspace/research_notes/drive-truth-campaign/TRUTH-LEDGER.md: verdict "QUEUED — text not extracted — QUEUED for content verdict." matches this log exactly, and the card's basis (binary present, extraction empty at 2 bytes, scanned document whose text layer did not extract, card written from filename and embedded PDF metadata only) matches the GAP-NOTE's account of it.
  4. Read the worklist row for census 117 in QUEUE-WORKLIST.json: Drive ID, filename, size 1673880, and not-trashed (LIVE) status all match this log.
  5. Checked for any other on-disk source holding this item's real text, by Drive ID, in the campaign work dirs extracts/, pdf/, and bin/: extracts/ holds no file for this Drive ID; pdf/ holds only the stated 2-byte extract; bin/ holds the PDF binary itself (1,673,880 bytes; pdfinfo title "CIA-UAP-010", 2 pages). No usable text source held by the campaign was omitted from the GAP-NOTE.
  6. Overstatement check: the GAP-NOTE attributes the subject description to the filename and the ledger card, claims no content assessment, and records no document-level errors finding. Nothing in the package overstates what exists.
  7. Addenda check: at verification time the staged package contained only GAP-NOTE.md and this AUDIT-LOG.md — no PAPER.md and no OCR-FINISH addendum was present to verify.
- Result: VERIFIED — claims measured and matching.

## ADDENDUM — 2026-10-16 (OCR-FINISH CREW, Drive Queued-695 Finishing Campaign)

- Action: the PDF was downloaded again from Drive via the Drive connector (file size returned 1,673,880 bytes, matching the worklist), because the gap recorded above was an extraction failure, not an absence of content.
- Download: /home/hatch/workspace/drive-truth-followthrough/work/downloads/117-1IAUmAsfe_rcBSMt9o1G9AsEXiffhqLYl.pdf
- Download SHA-256: 3abdbd131944fb847ec6eda8bf7f3f12684812bec71ea27c22ab5c3bb2ed4eb9
- PDF facts: 2 pages (pdfinfo); encrypted AES-256, print allowed, copy not allowed; pdftotext -layout again returned 2 bytes, confirming the copy restriction as the cause of the original empty extract.
- OCR method: pdftoppm -r 200 -png on all pages, then tesseract 5.3.4 per page, concatenated in page order to /home/hatch/workspace/drive-truth-followthrough/work/downloads/117-1IAUmAsfe_rcBSMt9o1G9AsEXiffhqLYl.txt. Page 1 yielded 859 OCR characters and page 2 yielded 3,825; final text read: 4,684 characters. The OCR text was cross-checked against the rendered page images, which the crew read directly to settle names, the report number (OO-B-321/23490-67), and the header block that the dark screened first page rendered poorly for OCR.
- Result: the OCR yielded real readable text. PAPER.md has been written in this folder to the Hundred-Draft standard for collected documents, and this finish supersedes the GAP-NOTE.md staged above. The GAP-NOTE and the original audit entries above are unchanged; a dated supersession line has been added at the top of the GAP-NOTE pointing to PAPER.md.
- Staging only: nothing was published, pushed, emailed, posted, uploaded, or deleted; the Drive item and the original on-disk extract were not altered.

## VERIFICATION ADDENDUM — 2026-10-16 (VERIFY CREW 5, Drive Queued-695 Finishing Campaign)

- Verifier name/crew: VERIFY CREW 5 (independent checker for the OCR-FINISH crew's work)
- Date: 2026-10-16
- Scope: verification of the OCR-FINISH addendum above and of PAPER.md. This crew did not edit PAPER.md or GAP-NOTE.md. The VERIFIER section above (VERIFY CREW 1's gap-note verdict) is left intact and is not overwritten by this addendum.
- Checks performed:
  1. Downloaded PDF at /home/hatch/workspace/drive-truth-followthrough/work/downloads/117-1IAUmAsfe_rcBSMt9o1G9AsEXiffhqLYl.pdf: SHA-256 recomputed as 3abdbd131944fb847ec6eda8bf7f3f12684812bec71ea27c22ab5c3bb2ed4eb9, matching the addendum's and PAPER.md's claim exactly. File size recomputed as 1,673,880 bytes, matching the claim. pdfinfo reports 2 pages, matching the claim.
  2. Encryption / copy-denied claim: pdfinfo reports "Encrypted: yes (print:yes copy:no change:no addNotes:yes algorithm:AES-256)", confirming the AES-256, print-allowed, copy-not-allowed claim. A fresh pdftotext -layout run on the downloaded PDF yielded exactly 2 bytes (two form-feed characters), confirming the claim that direct text extraction returns 2 bytes.
  3. OCR text file /home/hatch/workspace/drive-truth-followthrough/work/downloads/117-1IAUmAsfe_rcBSMt9o1G9AsEXiffhqLYl.txt: measured 4,684 by wc -c, and 4,684 by wc -m in the POSIX locale — the claimed figure. The per-page files agree: ocr117/p-1.txt is 859 and ocr117/p-2.txt is 3,825 by the same measure, summing to 4,684, and the combined file is byte-identical to the concatenation of p-1.txt followed by p-2.txt, in page order as claimed. Counting note, recorded for precision and not counted as a discrepancy (same basis as VERIFY CREW 1's counting note for census #118): a UTF-8 codepoint count returns 4,668, because page 1 contains eight multibyte punctuation characters (one em dash, seven curly quotation marks) counted once each as codepoints but as multiple bytes. The byte count, per-page split, content, and outcome are unaffected.
  4. Content match, OCR text: the OCR text itself contains Kozyrev (twice), Idlis (twice), the report-number suffix in the form "00-B-321,/23490-67", and the page-2 account that PAPER.md follows (Koval and the reddish object in the countryside, Galkin at Crimea, Idlis at Alma Ata conceding the question was "clearly still an open question", Lifschitz, Menzel's book, and the closing judgment on official treatment). The names Moroz and Pulkovo, the corrected report number, and the distribution date do not appear in the raw OCR text: page 1's OCR is fragmentary there, exactly as the addendum states.
  5. Content match, page image: this verifier read the rendered page-1 image (work/downloads/ocr117/p-1.png) directly. It shows "REPORT NO. OO-B-321/23490-67" (letter O twice, not zero-zero), "DATE DISTR. 18 AUG 67", "He visited V.I. Moroz, Sternberg Institute, Moscow, who was noncommittal on the subject of UFO's", a Pulkovo Observatory paragraph, and Kozyrev's personal opinion that UFOs may originate on Venus. PAPER.md's readings — Moroz, Kozyrev, Idlis; report number OO-B-321/23490-67; distribution date 18 August 1967 — match the printed page, and the addendum's statement that the page images were read to settle names, the report number, and the header block is confirmed. PAPER.md's Errors and anomalies section itself discloses that the OCR misread the report number as "00-B-321".
  6. Abstract length: the Abstract section of PAPER.md was counted at 204 words (whitespace split), within the required 150 to 250 words.
  7. Addendum discipline: compared against the pre-OCR state recorded in /home/hatch/workspace/drive-truth-followthrough/work/VERIFY-LOG-01.md. The original AUDIT-LOG sections (Source, Prior verdict, Checks performed, Corrections and judgment calls, Outcome) are present with their original content, including the original Outcome line "GAP-NOTE staged. No PAPER.md was created for this item."; VERIFY CREW 1's VERIFIER section is intact; the OCR-FINISH crew's work appears only as the dated addendum appended after it. GAP-NOTE.md carries exactly one added element, its top line: "> SUPERSEDED 2026-10-16: The PDF was downloaded again and read by OCR during the Drive Queued-695 Finishing Campaign. The finished assessment is PAPER.md in this folder. This gap note is retained unchanged as the record of the earlier state." The body of the GAP-NOTE below that line matches the pre-OCR account in VERIFY-LOG-01.md (subject attributed to filename and ledger card only, no content assessment claimed).
- Result: VERIFIED — claims measured and matching, with the counting note at item 3.
