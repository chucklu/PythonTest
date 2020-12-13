import re
rgx_pat = 'a(b|c)*d'
rgx = re.compile(rgx_pat, flags=re.IGNORECASE)
txt = 'ad,abd,acd,abbd,abcd,ACCD,acbccd,aed'
for mat in rgx.finditer(txt):
	print(mat.group())