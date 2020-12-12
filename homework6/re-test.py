import re
rgx_pat = 'a(b|c)*d'
txt = 'ad,abd,acd,abbd,abcd,accd,acbccd,aed'
mat = re.findall(rgx_pat, txt)
print(mat)

for mat in re.finditer(rgx_pat, txt):
    print(mat)