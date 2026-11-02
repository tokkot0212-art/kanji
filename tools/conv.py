import json,re,sys
src=open(sys.argv[1],encoding='euc_jisx0213',errors='ignore').read().splitlines()
n={};a={};mode=None
for line in src:
    if line.startswith(';; okuri-ari'): mode='a';continue
    if line.startswith(';; okuri-nasi'): mode='n';continue
    if not line or line.startswith(';'): continue
    k,_,rest=line.partition(' /')
    cands=[]
    rest=re.sub(r'\[[^\]]*\]','',rest)
    for c in rest.split('/'):
        c=c.split(';')[0].strip()
        if not c or c.startswith('(') or c in cands: continue
        if not re.search(r'[㐀-鿿豈-﫿々]',c): continue
        cands.append(c)
    if not cands: continue
    if mode=='a' and re.fullmatch(r'[ぁ-ゖー]+[a-z]',k): a[k]='/'.join(cands)
    elif mode=='n' and re.fullmatch(r'[ぁ-ゖー]+',k): n[k]='/'.join(cands)
json.dump({'n':n,'a':a},open(sys.argv[2],'w'),ensure_ascii=False,separators=(',',':'))
print(len(n),len(a),n.get('かんじ'),a.get('かk'))
