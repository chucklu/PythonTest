import re
txt = '''
This is a broken 
sentence.
This is another sentence.
'''
rgx_pat = r'(\w+ )\s*(\r)?\n\s*'
mats = re.finditer(rgx_pat, txt);
for mat in mats:
	print(mat)

txt = re.sub(rgx_pat, r'\1', txt)
print(txt)