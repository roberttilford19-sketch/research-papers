# INDEPENDENT DECODER REPORT — The Constitution of the United States Encoded in DNA Letters (full text, in silico)

This report was written by a separate decoder agent on 2026-11-14. The decoder, `decode_constitution_dna.py`, deposited with this report, was written from the specification alone — the codec statement, the sequence file, the source file of record, and the manifest figures — and from nothing else. Independence is the point of this lane, so the files the decoder agent did not read are named here in the same breath as that claim: it did not read `encode_constitution_dna.py`, it did not read `validate_constitution_dna.py`, it did not read `build_source.py`, and it did not read anything under the lane's `work/` folder. No encoder or validator code was imported, copied, or consulted at any point.

## The codec as implemented

Each byte becomes eight bits, most significant bit first. The eight bits are split into four pairs, and each pair maps to one base: 00 = A, 01 = C, 10 = G, 11 = T. One byte is therefore four bases. The decoder implements the exact inverse: A = 00, C = 01, G = 10, T = 11, with four bases making one byte and the most significant pair first. The sequence file is wrapped at 60 bases per line, and the decoder strips all whitespace before decoding. A separate small re-encoder, written inside the same script with its own independent logic — bit-mask extraction of the four two-bit fields of each byte by shifting and masking — is used only for the spot proofs in check (e), so that those proofs do not merely repeat the decoder's own table in reverse.

## Source of record

The source of record is `us-constitution-nara-transcription.txt`, the original byte stream the sequence claims to encode, deposited in this lane alongside the sequence file `constitution-dna-full.txt`. The manifest identifies that source as constructed from the National Archives founding-docs transcriptions at archives.gov — the Constitution transcription, the Bill of Rights transcription, and the Amendments 11–27 page — fetched 2026-11-14. This decoder took the deposited source file itself as the byte stream of record and compared against it directly, byte for byte and by hash.

## Figures computed by this decoder

The figures below are the decoder script's own printed output, copied exactly from its run.

- Total bases: 182384
- Alphabet: {A,C,G,T}
- Decoded bytes: 45596
- Source bytes: 45596
- SHA-256 of decoded stream: `5ba284d94d3f768de194b425edd4b48ca4ff65c7708d1fe454e4ef3d82899b07`
- SHA-256 of source stream, computed by this decoder: `5ba284d94d3f768de194b425edd4b48ca4ff65c7708d1fe454e4ef3d82899b07`
- SHA-256 of the base stream, computed by this decoder: `880e1058450f558eee9c264490307c475648034314aeee29b569225e4511ffd1`
- Manifest SHA-256 of the source byte stream: `5ba284d94d3f768de194b425edd4b48ca4ff65c7708d1fe454e4ef3d82899b07`
- Manifest SHA-256 of the base stream: `880e1058450f558eee9c264490307c475648034314aeee29b569225e4511ffd1`

## Checks

(a) Base count, alphabet, and divisibility — PASS. The base count is 182384, which equals 4 × 45596 source bytes exactly. The alphabet is exactly {A,C,G,T}, with no other character present after whitespace was stripped. The base count is divisible by 4.

(b) Full decode is valid UTF-8 — PASS. The complete decoded byte stream decodes as UTF-8 without error.

(c) Decoded bytes equal the source, and hashes agree — PASS. The decoded bytes equal the source file byte-for-byte, and the SHA-256 of the decoded stream, `5ba284d94d3f768de194b425edd4b48ca4ff65c7708d1fe454e4ef3d82899b07`, equals the SHA-256 of the source stream computed by this decoder, `5ba284d94d3f768de194b425edd4b48ca4ff65c7708d1fe454e4ef3d82899b07` — both figures computed by this decoder in the same run, stated here in the same breath as the claim.

(d) Manifest figures match — PASS. The manifest's source figure, `5ba284d94d3f768de194b425edd4b48ca4ff65c7708d1fe454e4ef3d82899b07`, matches this decoder's computed source hash, and the manifest's base-stream figure, `880e1058450f558eee9c264490307c475648034314aeee29b569225e4511ffd1`, matches this decoder's computed base-stream hash.

(e) Spot proofs by independent re-encoding — PASS. Using the separate re-encoder described above, the first 1,000 source bytes (byte offset 0, base offset 0), a 1,000-byte slice centered on the source midpoint (byte offset 22298, base offset 89192), and the last 1,000 source bytes (byte offset 44596, base offset 178384) were each re-encoded and each matched the sequence exactly at base offset = byte offset × 4.

## Verdict

A decoder written from the specification alone, without reading the encoder, the validator, the source builder, or any working file, recovered the source of record exactly: 182,384 bases decoded to 45,596 bytes, valid UTF-8, byte-for-byte identical to `us-constitution-nara-transcription.txt`, with the decoded hash, the source hash, and both manifest hashes all agreeing in the same run, and with three independent re-encoding spot proofs matching at the head, the middle, and the tail of the stream. The claim this deposit makes — that the base stream is a lossless encoding of that source under the stated codec — is therefore proved on this independent evidence, and no failing check stands against it.

VERDICT: PASS
