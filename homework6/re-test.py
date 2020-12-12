import re
rgx_pat = 'a(b|c)*d'
txt = 'ad,abd,acd,abbd,abcd,accd,acbccd,aed'
mat = re.search(rgx_pat, txt)
print(mat)
if(mat != None):
	print(mat.group())