import hashlib

CODEC = {'00':'A','01':'C','10':'G','11':'T'}
REV = {v:k for k,v in CODEC.items()}

def encode(data: bytes) -> str:
    out = []
    for b in data:
        bits = format(b, '08b')
        for i in range(0, 8, 2):
            out.append(CODEC[bits[i:i+2]])
    return ''.join(out)

def decode(dna: str) -> bytes:
    bits = ''.join(REV[c] for c in dna.strip())
    return bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))

def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def report(name, source_text):
    data = source_text.encode('utf-8')
    dna = encode(data)
    back = decode(dna)
    assert back == data, f"{name}: ROUND TRIP FAIL"
    gc = (dna.count('G') + dna.count('C')) / len(dna) * 100
    run = best = 1
    for i in range(1, len(dna)):
        run = run + 1 if dna[i] == dna[i-1] else 1
        best = max(best, run)
    print(f"{name}: {len(source_text)} chars, {len(data)} bytes, {len(dna)} bases, round-trip PASS, GC {gc:.4f}%, longest run {best}")
    print(f"  source SHA-256 {sha(data)}")
    print(f"  dna    SHA-256 {sha(dna.encode())}")
    return dna

# 1) Validate the encoder against the existing deposit of record
dep = '/home/hatch/workspace/research-papers/dna-codec-jirang-ge-qingyun-ge/'
for stem in ('jirang-ge', 'qingyun-ge'):
    src = open(dep + stem + '-source.txt', 'rb').read()
    dna_file = open(dep + stem + '-dna.txt').read().strip()
    mine = encode(src)
    print(f"VALIDATION {stem}: encoder reproduces shelf DNA exactly: {mine == dna_file}")

# 2) The modern-language renderings (desk draft, simplified characters)
jirang_modern = "太阳升起就下地干活，太阳落下就回家休息。挖井就有水喝，种地就有饭吃。皇帝的权力，对我来说又算得了什么呢！"
qingyun_modern = "祥云多么灿烂啊，缓缓地汇聚舒展啊。太阳和月亮的光辉，一天又一天地闪耀啊。"

for stem, text in (('jirang-ge-modern', jirang_modern), ('qingyun-ge-modern', qingyun_modern)):
    dna = report(stem, text)
    open(stem + '-source.txt', 'w', encoding='utf-8').write(text)
    open(stem + '-dna.txt', 'w').write(dna + '\n')
print("files written to ~/workspace/jirang-modern-companion/")
