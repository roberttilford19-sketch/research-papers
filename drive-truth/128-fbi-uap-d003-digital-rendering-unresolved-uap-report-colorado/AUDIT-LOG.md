# AUDIT LOG — Census #128

- **Item:** FBI-UAP-D003_Digital-Rendering_Unresolved-UAP-Report_ColoradoSprings_2022.pdf (ledger-card filename; see discrepancy note below)
- **Drive ID:** 1ljKihm3U08Z-aq29yqV3RVS1hCBNbcvg
- **Source text path:** /home/hatch/workspace/drive-truth-followthrough/work/downloads/128-1ljKihm3U08Z-aq29yqV3RVS1hCBNbcvg.txt
- **Source text sha256:** b0a0f3fccde2bde5a2974bca0d3d4e3b6c5e428af077fdc4c6da6381ca989e87
- **Source PDF path:** /home/hatch/workspace/drive-truth-followthrough/work/downloads/128-1ljKihm3U08Z-aq29yqV3RVS1hCBNbcvg.pdf
- **Source PDF sha256:** e067ec3753f24fbe26501a3932bce900124efea19ce5f949368f1b74d95fb53d
- **Source PDF measured properties:** 3,459,421 bytes; 1 page; page size 960.72 × 540.72 pts; internal title/subject "FBI-UAP-D003" (pdfinfo).
- **Chars read:** 124 — the entire OCR output file. It contains zero readable words; all 124 characters are recognition texture noise.
- **Ledger card:** [#128] in /home/hatch/workspace/research_notes/drive-truth-campaign/work/ledger_cards.json — LIVE, PDF 3.3 MB, modified 2026-06-23; summary describes an FBI UAP release set item, Colorado Springs incident (rendering).
- **Prior verdict:** QUEUED — text not extracted — QUEUED for content verdict.
- **Outcome:** FINISHED-STAGED as an identification package (PAPER.md). No text finish was possible; see judgment call.

## Judgment-call reasoning

The dispatch offered two honest stagings: an identification package, or a GAP-NOTE.md stating that no finish is possible. The identification package was chosen because the measured record is complete enough to identify the item truthfully — file size, hash, page count, dimensions, extraction history, and a directly inspected description of the image — and an identification package preserves that record for the collection in a way a bare gap note would not. The package is deliberately limited to what the evidence supports. It invents no provenance, no narrative, and no content. If a verifier judges that an image-only exhibit should carry a gap note instead, the audit record below contains everything needed to convert this package without new measurement.

Basis, from OCR-RESIDUE-LOG.md (the measured evidence base): the single page is a pure digital rendering / photographic image — landscape scene (mountain front, town, roadside guardrail) with a white oval object rendered in the sky. Visual inspection of the 300-dpi render by the OCR crew confirmed no text anywhere on the page. OCR output of 124 chars is tesseract texture noise from terrain detail, not words; a forced `--psm 6` pass produced ~2,007 chars of the same noise with zero readable words. TEXT-READY: NO — image-only exhibit; the rendering itself is the content. This crew additionally rendered the page at 72 dpi and inspected the image directly before writing the description in PAPER.md; the inspection agreed with the OCR crew's description in every particular.

## Corrections

None. No text exists to correct, and no wording in PAPER.md derives from the 124 noise characters.

## Unattributable claims

- Filename-year discrepancy: the ledger card records the filename as ending "ColoradoSprings_2022.pdf"; the dispatch record for this assignment gives "ColoradoSprings_2025.pdf". The PDF itself carries no date in its content and cannot settle which year the filename bears. PAPER.md uses the ledger-card filename and flags the discrepancy here; no year is asserted as fact anywhere in the package.
- Provenance: nothing in the file attributes the image to any author, agency action, date, or specific incident. The FBI UAP series and Colorado Springs associations rest solely on the filename and the ledger card and are framed that way in PAPER.md.
- Nature of the image: the file does not establish whether the image is a photograph, a constructed rendering, or a composite. PAPER.md calls it "a digital rendering or photographic image," following the OCR crew's wording, and draws no conclusion.

## Duplication note

No duplication suspected. The item is a companion exhibit within a numbered series — census #126 (FBI-UAP-D001 FD-302 report, Colorado Springs) and #127 (FBI-UAP-D002 FD-1057 report, Colorado Springs) are written reports in the same series, and #130 is an analysis of the Colorado Springs incident — but #128 shares no content with them; it is a standalone image with no text. Recorded as series context only, not as suspected duplication.

## Register rescan

PAPER.md framing prose rescanned after drafting: neutral, publication-ready register; no workshop, campaign, or military vocabulary about the work; no "first," "only," or "oldest" claims; every statement about the item is tied to a measurement, the OCR record, or direct inspection, and the filename/ledger associations are labeled as such rather than adopted as facts about the image.

## VERIFIER

- **VERIFIED — VERIFY CREW 11, 2026-10-16.** Independent recomputation and inspection, no edits to PAPER.md.
- **Hash/size/pages:** PDF sha256 recomputed `e067ec3753f24fbe26501a3932bce900124efea19ce5f949368f1b74d95fb53d` — matches this log; size **3,459,421 bytes** and **1 page** confirmed (pdfinfo: 960.72 × 540.72 pts, internal title/subject "FBI-UAP-D003," print:yes / copy:no — all as the paper states). Source-text sha256 also recomputed and matches (`b0a0f3fccde2bde5a2974bca0d3d4e3b6c5e428af077fdc4c6da6381ca989e87`, 124 bytes).
- **Independent render and inspection:** `pdftoppm` could not write in this session because /tmp was 100% full (tmpfs 512M), so the page was rendered independently with PyMuPDF at 150 dpi (2002 × 1127 px, embedded image 2002 × 1128; render kept at `work/v11-render/128-page1-150dpi.png`) and inspected directly. The paper's description is **confirmed in every particular**: a clear blue sky over a steep rocky mountain front filling the middle distance; a small town of low houses at its foot; grassland, a metal roadside guardrail and a strip of pavement across the immediate foreground; and a **single white, mottled/textured, oval object** in the sky above and in front of the mountain front, roughly centred, with no visible markings. **No text anywhere on the page** — no caption, label, stamp, or lettering of any kind.
- **Independent OCR:** verifier's own tesseract pass on that render returned 40 characters of fragment noise (e.g. "eer Bava oe? Sa / CATT Vis hs nD") with **zero readable words** — the same texture-noise character as the finisher's 124-character pass and forced pass. The PDF has no text layer (extracted text length 0). The null-text finding is confirmed.
- **No invention:** confirmed — PAPER.md asserts no provenance, narrative, date, authorship, location, or incident connection beyond the filename/ledger association, which it labels as such; it does not determine what the depicted object is or whether the image is a photograph or a constructed rendering. On the flagged year conflict, the paper gives the filename only in its ledger-card form ("…ColoradoSprings_2022.pdf," expressly attributed to the ledger card with a pointer to this log's discrepancy note on the dispatch record's 2025 form) and **asserts no year as fact** anywhere; the file itself carries no date, as this log states.
- No discrepancy found. Verifier does not change status; coordinator books the verdict from VERIFY-LOG-11.md.
