import re
rgx_pat = 'a(b|c)*d'
rgx = re.compile(rgx_pat, flags=re.IGNORECASE)
txt = 'ad,abd,acd,abbd,abcd,ACCD,acbccd,aed'
mat = rgx.search(txt, pos=10)
print(mat)
mat_1 = rgx.search(txt, endpos=2)
print(mat_1)