#!/usr/bin/env python3
"""House codec: UTF-8 bytes -> bits -> 00=A, 01=C, 10=G, 11=T.
Encodes the two settled poem texts, writes the .dna.txt sequence files,
then decodes them back independently and asserts byte-identical round trip."""
import hashlib, pathlib

HERE = pathlib.Path(__file__).parent
MAP = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
REV = {v: k for k, v in MAP.items()}

def encode(data: bytes) -> str:
    out = []
    for byte in data:
        bits = f'{byte:08b}'
        for i in range(0, 8, 2):
            out.append(MAP[bits[i:i+2]])
    return ''.join(out)

def decode(seq: str) -> bytes:
    bits = ''.join(REV[ch] for ch in seq)
    return bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))

for name in ('jirang-ge', 'qingyun-ge'):
    text = (HERE / f'{name}-source.txt').read_text(encoding='utf-8').strip()
    data = text.encode('utf-8')
    seq = encode(data)
    (HERE / f'{name}-dna.txt').write_text(seq + '\n', encoding='utf-8')
    back = decode(seq)
    ok = back == data and back.decode('utf-8') == text
    longest = max(len(run) for ch in 'ACGT' for run in seq.split(ch)[0:0]) if False else 0
    # longest homopolymer run
    run = best = 1
    for a, b in zip(seq, seq[1:]):
        run = run + 1 if a == b else 1
        best = max(best, run)
    print(f'{name}: chars={len(text)} bytes={len(data)} bases={len(seq)} '
          f'sha256={hashlib.sha256(data).hexdigest()} roundtrip={"PASS" if ok else "FAIL"} '
          f'longest_homopolymer_run={best}')
    print(f'  text: {text}')
    assert ok
print('ALL ROUND TRIPS PASS')
