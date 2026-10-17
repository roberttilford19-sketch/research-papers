# AUDIT LOG — Census #12, app-release.aab

- **Source file path:** /home/hatch/workspace/drive-truth-followthrough/work/downloads/12-1WrBlkAovVcdrv1ZksBU0y9iTwMoPn5P2.aab
- **Source file sha256:** a23440ed5afa9fedf61368642cd33d8a45586ab4683880656af996baab6e51cb (from FETCH-LOG-wave01.md, Fetch Crew 1; recomputed at this desk and matched)
- **Bytes:** 15,289. No text exists to read; the item is a binary archive.
- **Ledger card prior verdict:** QUEUED — at ledger time no downloaded copy existed and no read was possible; the card noted that census #12 and #54 share name and size (15,289 bytes) and might be copies of each other.
- **Pattern applied:** Identification package, per dispatch. PAPER.md is an identification record, not a finished document: file identity, size, hash, an explanation of the format, and build metadata read from the package.

## Method

The archive was listed with a ZIP directory listing only, and the binary AndroidManifest.xml and BundleConfig.pb entries were read as data and decoded (string extraction plus a generic protobuf field walk for the manifest attributes). Nothing in the bundle was executed, installed, or decompiled. The signing entries were listed but the certificate was not examined. Minimum and target SDK attributes were not extracted for this build; PAPER.md states that limit.

## Corrections

None. No text was corrected; the source file and the Drive original are unaltered.

## Factual claims not attributable

- None introduced by this desk. Identity facts come from FETCH-LOG-wave01.md and the file on disk; Drive path, modified date, and state come from the ledger card; build metadata comes from the package's own manifest as decoded.

## Suspected duplication

Census #54 is SUSPECTED-DUPLICATE-OF census #12. Evidence: FETCH-LOG-wave01.md records Fetch Crew 1's comparison — both files hash to a23440ed5afa9fedf61368642cd33d8a45586ab4683880656af996baab6e51cb at 15,289 bytes, comparison verdict "IDENTICAL" — and this desk recomputed both hashes from the downloaded files with the same result. The two bundles' archive listings are also entry-for-entry identical. The duplicate verdict itself comes at verification, not from this crew.

## Register rescan

PAPER.md was rescanned after drafting: neutral, publication-ready register; no workshop, campaign, or military vocabulary about the work; no "first / only / oldest" claims made.

## VERIFIER

(Left blank — verification is a separate pass by a different crew.)

- **2026-10-16 — VERIFY CREW 7: VERIFIED.** Source file sha256 recomputed from the downloaded .aab: a23440ed5afa9fedf61368642cd33d8a45586ab4683880656af996baab6e51cb — matches this log exactly. Size remeasured: 15,289 bytes, matching. Archive listing independently read by this verifier: 10 entries, including base/dex/classes.dex at 2,352 bytes and base/assets/index.html at 20,006 bytes, as PAPER.md states. No Abstract applies (identification package, per dispatch). The suspected-duplication note concerning census #54 is accurate and is ruled on in the census #54 entry and in VERIFY-LOG-07.md: census #54 is a duplicate of this file. Register rescan confirmed (the one occurrence of "Crew" is the citation of Fetch Crew 1's recorded comparison in FETCH-LOG-wave01.md).
