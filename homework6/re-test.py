import re
rgx_pat = 'a(b|c)*d'
rgx = re.compile(rgx_pat, flags=re.IGNORECASE)
txt = 'ad,abd,acd,abbd,abcd,ACCD,acbccd,aed'
mat = rgx.match(txt, pos=3)
print(mat)
mat_1 = rgx.match(txt, endpos=1)
print(mat_1)