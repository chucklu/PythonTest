import re
txt = '<hello>,hello!'
rgx_pat = r'(<)?hello(?(1)>|!)'
for mat in re.finditer(rgx_pat, txt):
	print(mat.group())