# AUDIT LOG — Census #10, app-release-api36.aab

- **Source file path:** /home/hatch/workspace/drive-truth-followthrough/work/downloads/10-16IoekWqVT-VgrWbSXh4jPsxPGUWT0BPJ.aab
- **Source file sha256:** 1b42b0b98f227c38549136fce0162b14cbb0ff9aa4fa9ab7b03bf754873902b1 (from FETCH-LOG-wave01.md, Fetch Crew 1; recomputed at this desk and matched)
- **Bytes:** 15,323. No text exists to read; the item is a binary archive.
- **Ledger card prior verdict:** QUEUED — at ledger time no downloaded copy existed and no read was possible; the card noted that census #12 and #54 share name and size and might be copies of each other.
- **Pattern applied:** Identification package, per dispatch. PAPER.md is an identification record, not a finished document: file identity, size, hash, an explanation of the format, and build metadata read from the package.

## Method

The archive was listed with a ZIP directory listing only, and the binary AndroidManifest.xml and BundleConfig.pb entries were read as data and decoded (string extraction plus a generic protobuf field walk for the manifest attributes). Nothing in the bundle was executed, installed, or decompiled. The signing entries were listed but the certificate was not examined.

## Corrections

None. No text was corrected; the source file and the Drive original are unaltered.

## Factual claims not attributable

- None introduced by this desk. Identity facts come from FETCH-LOG-wave01.md and the file on disk; Drive path, modified date, and state come from the ledger card; build metadata comes from the package's own manifest as decoded. The statement that this build is the later of the two release builds rests on the two packages' declared version codes, version names, and compile SDK levels, all read from the packages themselves.

## Suspected duplication

Not a duplicate of census #12 or #54: its hash differs from theirs, and its declared version (1.0.1, versionCode 2, compileSdkVersion 36) differs from census #12's (1.0, versionCode 1, compileSdkVersion 35).

## Register rescan

PAPER.md was rescanned after drafting: neutral, publication-ready register; no workshop, campaign, or military vocabulary about the work; no "first / only / oldest" claims made.

## VERIFIER

(Left blank — verification is a separate pass by a different crew.)

- **2026-10-16 — VERIFY CREW 7: VERIFIED.** Source file sha256 recomputed from the downloaded .aab: 1b42b0b98f227c38549136fce0162b14cbb0ff9aa4fa9ab7b03bf754873902b1 — matches this log exactly. Size remeasured: 15,323 bytes, matching. Archive listing independently read by this verifier: 10 entries, including base/dex/classes.dex at 2,364 bytes and base/assets/index.html at 20,006 bytes, as PAPER.md states. No Abstract applies (identification package, per dispatch). **Not a duplicate of census #12 or #54, confirmed:** this file's size (15,323 bytes) and hash differ from theirs (15,289 bytes; a23440ed…), its bytes differ from census #12's on direct comparison, its signing entries carry different timestamps (2026-10-08 against 2026-10-04), and its classes.dex differs in size and CRC. Register rescan confirmed.
