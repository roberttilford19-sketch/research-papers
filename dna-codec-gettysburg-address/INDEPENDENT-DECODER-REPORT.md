# Independent Decoder Report — Gettysburg Address DNA Lane

Date: 2026-11-14

## Independence Statement

This decoder was written from the written specification alone. The following files were not read, imported, or copied: `~/workspace/dna-gettysburg-2026-11-14/encode_gettysburg_dna.py`, `~/workspace/dna-gettysburg-2026-11-14/validate_gettysburg_dna.py`, and anything under `~/workspace/dna-gettysburg-2026-11-14/work/`. The decoder is deposited at `~/workspace/dna-gettysburg-2026-11-14/decode_gettysburg_dna.py` and was run by the separate decoder agent to perform the checks below.

## Codec As Implemented

Each base is two bits — A=00, C=01, G=10, T=11. Four bases make one byte, most significant pair first: the decoder maps each base to its two-bit value, shifts and ORs the four values in order into one byte, and repeats over the whole stream. The sequence file was read and all whitespace was stripped before decoding. The spot-proof re-encoder inside the same script uses independent bit-extraction logic: it converts each byte to an eight-character binary string with `format(byte, "08b")`, slices that string into two-character chunks, and maps each chunk string ("00", "01", "10", "11") to a base (A, C, G, T respectively).

## Source of Record

- Sequence file: `~/workspace/dna-gettysburg-2026-11-14/gettysburg-dna.txt`
- Source file: `~/workspace/dna-gettysburg-2026-11-14/gettysburg-address-source.txt`
- Manifest: `~/workspace/dna-gettysburg-2026-11-14/MANIFEST-DNA-GETTYSBURG.md`
- Decoder: `~/workspace/dna-gettysburg-2026-11-14/decode_gettysburg_dna.py`

## Figures Computed

- Total bases: 5876
- Expected base count: 5876
- Alphabet: {A, C, G, T}
- Decoded bytes: 1469
- Source bytes: 1469
- SHA-256 of decoded stream: `809838efd41698422636fb2df8bebe2a7e8c29a3baf109b3bdceed6812266903`
- SHA-256 of source (computed from the source file as read from disk): `809838efd41698422636fb2df8bebe2a7e8c29a3baf109b3bdceed6812266903`
- SHA-256 of base stream (computed over the stripped bases as ASCII): `b4a32368d2a81f755ca5cae9efc62a15e81a9d8fee3ca3f9f2a9138764ba71a1`
- SHA-256 of the source byte stream, as printed in the manifest: `809838efd41698422636fb2df8bebe2a7e8c29a3baf109b3bdceed6812266903`
- SHA-256 of the base stream, as printed in the manifest: `b4a32368d2a81f755ca5cae9efc62a15e81a9d8fee3ca3f9f2a9138764ba71a1`

## Checks

- (a) Base count, alphabet, and divisibility — PASS. Total bases 5876 equals the expected count 5876; the alphabet is exactly {A, C, G, T}; 5876 is divisible by 4 (5876 / 4 = 1469).
- (b) Valid UTF-8 — PASS. The full decoded stream of 1469 bytes decodes as valid UTF-8 with no error.
- (c) Decoded equals source — PASS. The decoded bytes equal the source file byte-for-byte (1469 bytes against 1469 bytes), and SHA-256 of the decoded stream `809838efd41698422636fb2df8bebe2a7e8c29a3baf109b3bdceed6812266903` equals SHA-256 of the source as read from disk `809838efd41698422636fb2df8bebe2a7e8c29a3baf109b3bdceed6812266903`.
- (d) Manifest figures — PASS. The source SHA-256 parsed from the manifest, `809838efd41698422636fb2df8bebe2a7e8c29a3baf109b3bdceed6812266903`, matches the computed source SHA-256, and the base-stream SHA-256 parsed from the manifest, `b4a32368d2a81f755ca5cae9efc62a15e81a9d8fee3ca3f9f2a9138764ba71a1`, matches the computed base-stream SHA-256 over the stripped bases as ASCII.
- (e) Spot proofs — PASS. Using the separately written re-encoder inside the decoder script: the first 300 source bytes (byte offset 0, bases 0–1199) re-encode to exactly the corresponding sequence slice; a 300-byte chunk centered on the file midpoint (byte offset 584, bytes 584–883, bases 2336–3535) re-encodes to exactly the corresponding sequence slice; and the last 300 source bytes (byte offset 1169, bytes 1169–1468, bases 4676–5875) re-encode to exactly the corresponding sequence slice. All three comparisons matched, 1200 bases against 1200 bases in each case.

## Verdict

Every check (a)–(e) passed: the base stream of 5876 bases over the alphabet {A, C, G, T} decodes under the stated codec to exactly the 1469 source bytes, valid UTF-8, with both SHA-256 figures matching the manifest.

VERDICT: PASS
