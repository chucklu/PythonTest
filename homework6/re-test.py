import re
txt = 'John is the the instructor.'
rgx_pat = r'\b(?P<word>\w+)\s+\1'
mat = re.search(rgx_pat, txt)
if mat:
	print(mat.group('word'))