import re
txt = '<hello>,hello!'
rgx_pat = r'(<)?hello(?(1)>|!)'
for mat in re.finditer(rgx_pat, txt):
	print(mat.group())

rgx_pat2 = 'hello(?=!)'
for mat in re.finditer(rgx_pat2, txt):
	print(mat.span(), mat.group())

rgx_pat3 = 'hello(?!!)'
for mat in re.finditer(rgx_pat3, txt):
	print(mat.span(), mat.group())