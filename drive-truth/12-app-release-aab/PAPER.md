# Identification Record — app-release.aab (Census #12)

## Identification

- **Census #:** 12
- **Drive filename:** app-release.aab
- **Drive path (per the ledger card):** Inner Room Play app file/app-release.aab
- **Item type:** Android App Bundle (.aab), a binary application package. It contains no readable document text.
- **File size:** 15,289 bytes (downloaded copy on disk; the ledger card rounds this to 14.9 KB).
- **SHA-256:** a23440ed5afa9fedf61368642cd33d8a45586ab4683880656af996baab6e51cb (from FETCH-LOG-wave01.md; recomputed at this desk from the downloaded file and matched).
- **Drive state:** LIVE (per the ledger card in TRUTH-LEDGER.md).
- **Label:** Identification record for a binary build artifact in Robert Tilford's Drive. Staged desk copy prepared 2026-10-16 from Robert Tilford's Drive; original unaltered; AI assistance disclosed.

## Premise

This record identifies the earlier of the two release builds of "The Secret Teachings of Jesus" (the Inner Room app) held in Robert Tilford's Drive. Census #10, named app-release-api36.aab, is its successor build; this package is the original release build from which that successor was incremented, as the version metadata inside the two packages shows.

## What an Android App Bundle Is

An Android App Bundle is the publishing format Google Play requires for new applications. It is a signed archive, structured as a ZIP file, that contains an application's compiled code, resources, and manifest in modular form; Google Play's systems generate the actual installable packages for each device from the bundle. A bundle is therefore a distribution artifact rather than a document: it cannot be read as text, and it is not installed directly by end users. Identifying one means recording its file identity and the build metadata declared inside it, which is what this record does. Nothing inside the bundle was executed in preparing this record; the archive's file listing was read and its manifest metadata was decoded as data only.

## Build Metadata Read from the Package

The archive contains ten entries. Its contents are a base module holding the application: a compiled code file (base/dex/classes.dex, 2,352 bytes), a web asset (base/assets/index.html, 20,006 bytes) that carries the application's content, a launcher icon, the binary manifest (base/manifest/AndroidManifest.xml), and the bundle's resource and configuration tables. The signing block entries (META-INF/MANIFEST.MF, META-INF/INNERROO.SF, and META-INF/INNERROO.RSA) carry internal archive timestamps of 2026-10-04 19:44, while the ledger card records the Drive file's modified date as 2026-10-08. The manifest declares the following, as decoded from the package: application package name com.tilford.innerroom; versionName 1.0; versionCode 1; compileSdkVersion 35; platformBuildVersionName 15; and application backup disabled (allowBackup set to false). Minimum and target SDK values were not extracted for this build in this pass. The bundle configuration records bundletool version 1.17.2. The package name com.tilford.innerroom matches the Inner Room application's known package identity, and the web asset inside this bundle is the same size, to the byte, as the web asset inside census #10, while the compiled code file differs slightly (2,352 bytes here against 2,364 bytes in census #10), which is consistent with a version increment that changed build configuration more than content.

## Relation to Census #54

FETCH-LOG-wave01.md records a hash comparison run by Fetch Crew 1: census #12 and census #54 have the same SHA-256, a23440ed5afa9fedf61368642cd33d8a45586ab4683880656af996baab6e51cb, and the same size, 15,289 bytes, and the fetch log's comparison verdict is "IDENTICAL." This desk recomputed both hashes from the downloaded files and obtained the same result. On that evidence, census #54 is recorded in its own package as SUSPECTED-DUPLICATE-OF census #12; the duplicate verdict itself is reserved for the verification pass, not made here.

## Limits

This record identifies the bundle as a file; it does not audit the application it contains. The compiled code was not executed, decompiled, or reviewed, and the web asset inside the bundle was not separately assessed as a document. The signing certificate inside the package was not examined beyond noting the signing entries' presence and timestamps, so this record makes no statement about who signed the build. Minimum and target SDK versions were not extracted for this build. The build metadata above is what the package's own manifest declares, decoded from the binary manifest as data.
