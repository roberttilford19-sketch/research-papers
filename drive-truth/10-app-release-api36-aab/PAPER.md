# Identification Record — app-release-api36.aab (Census #10)

## Identification

- **Census #:** 10
- **Drive filename:** app-release-api36.aab
- **Drive path (per the ledger card):** Inner Room Play app file/app-release-api36.aab
- **Item type:** Android App Bundle (.aab), a binary application package. It contains no readable document text.
- **File size:** 15,323 bytes (downloaded copy on disk; the ledger card rounds this to 15.0 KB).
- **SHA-256:** 1b42b0b98f227c38549136fce0162b14cbb0ff9aa4fa9ab7b03bf754873902b1 (from FETCH-LOG-wave01.md; recomputed at this desk from the downloaded file and matched).
- **Drive state:** LIVE (per the ledger card in TRUTH-LEDGER.md).
- **Label:** Identification record for a binary build artifact in Robert Tilford's Drive. Staged desk copy prepared 2026-10-16 from Robert Tilford's Drive; original unaltered; AI assistance disclosed.

## Premise

This record identifies one of the application packages Robert Tilford prepared for "The Secret Teachings of Jesus" (the Inner Room app) during its Google Play closed-testing setup in October 2026. The filename's "api36" marker and the build metadata read from the package agree: this is the later of the two release builds in the Drive, compiled against Android API level 36, where the earlier build (census #12) was compiled against API level 35.

## What an Android App Bundle Is

An Android App Bundle is the publishing format Google Play requires for new applications. It is a signed archive, structured as a ZIP file, that contains an application's compiled code, resources, and manifest in modular form; Google Play's systems generate the actual installable packages for each device from the bundle. A bundle is therefore a distribution artifact rather than a document: it cannot be read as text, and it is not installed directly by end users. Identifying one means recording its file identity and the build metadata declared inside it, which is what this record does. Nothing inside the bundle was executed in preparing this record; the archive's file listing was read and its manifest metadata was decoded as data only.

## Build Metadata Read from the Package

The archive contains ten entries. Its contents are a base module holding the application: a compiled code file (base/dex/classes.dex, 2,364 bytes), a web asset (base/assets/index.html, 20,006 bytes) that carries the application's content, a launcher icon, the binary manifest (base/manifest/AndroidManifest.xml), and the bundle's resource and configuration tables. The signing block entries (META-INF/MANIFEST.MF, META-INF/INNERROO.SF, and META-INF/INNERROO.RSA) carry internal archive timestamps of 2026-10-08 06:57, consistent with the ledger card's modified date of 2026-10-08. The manifest declares the following, as decoded from the package: application package name com.tilford.innerroom; versionName 1.0.1; versionCode 2; compileSdkVersion 36; platformBuildVersionName 16; minimum SDK version 24; target SDK version 36; and application backup disabled (allowBackup set to false). The bundle configuration records bundletool version 1.17.2. The package name com.tilford.innerroom matches the Inner Room application's known package identity, and the version sequence — versionCode 2, version 1.0.1, API 36 — places this bundle one step after census #12 (versionCode 1, version 1.0, API 35), which is also what the two filenames suggest.

## Limits

This record identifies the bundle as a file; it does not audit the application it contains. The compiled code was not executed, decompiled, or reviewed, and the web asset inside the bundle was not separately assessed as a document. The signing certificate inside the package was not examined beyond noting the signing entries' presence and timestamps, so this record makes no statement about who signed the build. The build metadata above is what the package's own manifest declares; it was decoded from the binary manifest as data, and no other tool independently confirmed it.
