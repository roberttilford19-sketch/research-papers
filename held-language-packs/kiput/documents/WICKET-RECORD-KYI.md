# WICKET RECORD — KIPUT (KYI) LANE — THIN-BASE STOP, NO BUILD

**Lane:** Kiput — folder `~/workspace/ayah-kiput`, code KYI, lc kyi, scout Class 3 row §6a #9.
**Outcome:** STOPPED under the lane's thin-base rule (step 10 of the brief). No lexicon, styleguide, engine, build, assembly, verification, checker run, Purple measurement, glossary or flags were produced, because the base cannot ground the draft. Nothing was shelved or landed; no landing record, push script or finish script was run.

## What the base actually is — a correction to the brief, in the same breath as the stop

The brief named the base as Robert Blust, *A Dictionary of Kiput (with an English–Kiput finderlist)*, PL-546, ANU, "~2,100 words". The book that PL-546 actually is — verified on its own title page and preface as read at the desk — is Robert Blust, *A short morphology, phonology and vocabulary of Kiput, Sarawak* (Pacific Linguistics 546, The Australian National University, 2003; viii + 102 pages; ISBN 0 85883 536 3; DOI 10.15144/PL-546; online edition licensed 2015 CC BY-SA 4.0). There is no English–Kiput finderlist in it: its vocabulary (book pp. 43–101) runs Kiput–English only. Blust's own count, stated by him at §5.2 (book p. 42), is a **total vocabulary of 931 items collected**, of which 119 are probable loanwords, mostly from Brunei Malay. The materials rest on 20–25 hours of elicitation in 1971, primarily from one 17-year-old speaker, John Malang, with additional material from Thomas Belulok, then about 16. The "~2,100 words" figure in the brief is not supported by the book itself.

## How the text was reached

1. The ANU item page named in the brief — https://openresearch-repository.anu.edu.au/items/005e2411-1145-48fc-b36a-3c3791fd75f0 — was opened first, as instructed. It resolved to the correct item (title as above), but its fetched text carried only the repository's cultural-advice header (10 lines) and no bitstream link, so no PDF URL could be taken from the page's links by the desk's usual pattern.
2. One attempt to list the item's bitstreams through the repository's server API failed with an upstream fetch error and was not retried.
3. The full text was then resolved lawfully through the book's own DOI, https://doi.org/10.15144/PL-546, which browser.open read in full: 7,808 extracted lines, the complete book including the Kiput–English vocabulary at lines 2326–7808 (book pp. 43–101). The same full text is mirrored on Scribd as "Vocabulary of Kiput" (8,412 lines), which corroborates the contents. Working notes extracted from the text are saved at `work/base/base-notes-kyi.txt`.

## What was verified before the stop

- Master verification passed: MD5 of `~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md` = 064ee170806bb31f5bac3e75d2aa4d94, machine-computed.
- Lane setup was completed and stands in the folder: `python3 ~/workspace/.tools/gap-tier1/extract.py ayah-kiput/work` produced meta.json with **114 surahs, verses summing to 6,236, and 114 files in work/en/** — all three figures machine-asserted. These extraction outputs are the only build-side artifacts in the lane.

## The counts that force the stop

- Template key set (model lane `dict_mbf.py`): **1,887 keys**.
- Absolute ceiling: Blust's whole vocabulary is **931 items**, affixed sub-entries included in his presentation — even a perfect one-to-one mapping of every Kiput item onto a distinct template key could not reach the brief's ~600-key threshold by a safe margin, and most of the vocabulary is longhouse, riverine, flora and fauna vocabulary that matches no Quran core key.
- Sample count: the vocabulary's letters A–B (book pp. 43–50, about 90 headword bases) were read in full and matched generously against the 1,887 keys: roughly **35–40 matches, about 40%**, which extrapolates to roughly **370 grounded keys** over the whole vocabulary — far below ~600.
- Theological core, searched across the full text: **no attestation at all** for God, god, heaven, hell, angel, prayer, forgive, mercy, prophet, Lord, soul or king (the only "king" hits are "kingfisher" and verb endings; the only "hell" hit is "shell"). "Spirit" appears once, as akaaŋ 'ghost, spirit of the dead'. "Believe" appears only inside mufiew 'to doubt, to disbelieve'. Attested and usable, but far too few to carry a scripture draft: truth (tu'unaw/tunaw), hope/trust (araap, a Malay loan), book (bup, an English loan), die/death (m-ataay / p-ataay), and the pronoun and possessive system (possession by postposed pronoun — mateh kaw 'my eye' — with no 'punya' construction attested).

## Why the lane cannot proceed on this base

The brief's step 3 requires the God-word and Lord-word to be settled from what Blust attests, loans included. Blust attests neither word, in any form, native or loaned. A Kiput draft built anyway would have to invent its God-word, its Lord-word, and the whole theological register — exactly what the house rule forbids ("Never invent; Blust's headword spelling governs"). Combined with a grounded-key count of roughly 370 against a 1,887-key template, the draft would be mostly transliteration fallback wearing a Kiput label. The honest act is the stop.

## What would reopen this wicket

A larger Kiput lexical source: a fuller dictionary, a Kiput Bible portion or lectionary from the largely Catholic Kiput community of Long Kiput / Kuala Tutoh on the Baram River (which would also settle the God-word and Lord-word from living community usage), or Berawan–Kiput materials beyond PL-546. Any of those is a new base decision for Robert, not a desk improvisation.

Lane identity: Kiput (kyi), Berawan–Lower Baram, Baram River, Sarawak — Malaysia scout 2026-11-14, Class 3 row §6a #9. No first-translation claim is made by this record; the standing wording remains: none found after research (Malaysia scout, 2026-11-14).
