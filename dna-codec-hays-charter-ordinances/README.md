# The Charter Ordinances of the City of Hays, Kansas — in DNA Letters

**DNA work 16 in Robert Tilford's DNA-codec series. Built and shelved 2026-11-16.**

This folder holds the Charter Ordinances of the City of Hays, Kansas, as
published in the City's own Document Center, transcribed into the four DNA
letters A, C, G, and T. It is a gift deposit: the ordinances are the city's
public law, and this encoding is given freely to anyone who finds it.

## Files

- `hays-charter-ordinances-source.txt` — the source text: a plain header,
  then the six ordinance documents in ordinance-number order, each under a
  separator naming its Document Center source. The text of each ordinance
  was extracted from the City's own PDF (pdftotext, layout preserved) and
  is reproduced as extracted.
- `hays-charter-ordinances-dna.txt` — the same text in DNA letters,
  wrapped at 80 letters per line.

## The codec, in plain words

Take the text as UTF-8 bytes. Write each byte as eight bits. Read the bits
two at a time and write one DNA letter for each pair: 00 = A, 01 = C,
10 = G, 11 = T. Nothing is compressed and nothing is hidden: anyone holding
the letters and this rule can rebuild the source text exactly. This is an
**encoding, not a translation**. The deposit is a letter sequence only —
**no physical DNA exists, and none is made or implied.**

## Figures and verification

- Source text: 37,329 bytes (37,231 characters, header and separators
  included; the six ordinance texts alone are 32,027 characters).
  SHA-256: `e79b8d99eeb9e5173900be53a224969111a7d9af8069fabb0071fc92d0f6996a`
- DNA sequence: **149,316 bases**. SHA-256 of the letter string:
  `6e22f85142e79e9b72ff3a996ce40f6b17df1094603793449b5e4ab063244b2d`
  GC content 51.85%; longest homopolymer run 7.
- **Round trip: PASS.** The sequence was decoded back to bytes and compared
  with the source: byte-for-byte identical (matching SHA-256), verified
  twice — once inside the house encoder and once by an independent decode
  of the deposited DNA file.

## Provenance

City of Hays Document Center (haysusa.com/DocumentCenter), fetched
2026-11-16:

- Charter Ordinance No. 30 — document 5315 —
  https://www.haysusa.com/DocumentCenter/View/5315/Charter-Ordinance-No-30
- Charter Ordinance No. 31 — document 5316 —
  https://www.haysusa.com/DocumentCenter/View/5316/Charter-Ordinance-No-31
- Charter Ordinance No. 32 — documents 6573, 6603, and 6621 (three uploads) —
  https://www.haysusa.com/DocumentCenter/View/6573/Charter-Ordinance-No-32 ·
  https://www.haysusa.com/DocumentCenter/View/6603/Charter-Ordinance-No-32 ·
  https://www.haysusa.com/DocumentCenter/View/6621/Charter-Ordinance-No-32
- Charter Ordinance No. 33 — document 6753 —
  https://www.haysusa.com/DocumentCenter/View/6753/Charter-Ordinance-No-33-Increasing-TGT-Rates

## Ordinance inventory — including the gap

The Document Center set encoded here: **No. 30** (exempting the City from
K.S.A. 14-1501 through 14-1504; passed December 8, 2022), **No. 31**
(exempting the City from K.S.A. 12-1040; passed December 8, 2022),
**No. 32** (exempting the City from K.S.A. 14-570 and 14-571, public
improvements and bonds; passed July 25, 2024), and **No. 33** (transient
guest tax, amending No. 28; passed October 24, 2024).

Charter Ordinance No. 32 stands in the Document Center in three uploads.
The ordinance text is the same in all three; they differ only in the
publication dates stated in the heading line and in the clerk's Certificate
of No Protest (July 26 & August 2, 2024 in document 6573; August 7 &
August 14, 2024 in the heading of 6603 and in both places in 6621; 6603's
certificate still reads July 26 & August 2). All three uploads are encoded
here, each labeled, so the variance is preserved rather than resolved.

**The gap, stated plainly:** the City's charter ordinances run from No. 1
(1967) to No. 33 (2024) — the Kansas Secretary of State's *Index of City
Charter Ordinances* lists Hays Nos. 1–14 and 26–32, and No. 33's own
recitals cite Nos. 19, 23, and 28. The Document Center publishes standalone
documents for Nos. 30–33 only. **Charter Ordinances Nos. 1–29 are not in
this deposit, because the City does not publish them in its Document
Center.** This inventory was verified on 2026-11-16 against every Document
Center document reachable or indexed from this desk (including the Wayback
Machine's crawl index of the Document Center); the Document Center's own
folder-listing service could not be read from this network on that date
(its data calls are POST requests, which this connection drops), so the
inventory is graded complete-as-reachable, not certified against the live
folder listing.

## Rights and credit

The ordinances are public municipal documents of the City of Hays, Kansas.
This encoding is © Robert Tilford — **given free, never sold; attribution
requested.**

Encoded at the direction of **Robert Tilford, Hays, Kansas**, by
**Awen by Muse by Meta**. Nothing was sent to the City; the deposit itself
is the gift, shelved quietly for whoever searches for it.
