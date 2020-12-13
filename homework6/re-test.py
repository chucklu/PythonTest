import re
txt = '这句话既有English，又有Chinese。'
rgx_pat= r'[\u4e00-\u9fa5]' #简体汉字
rgx = re.compile(rgx_pat)
for mat in rgx.finditer(txt):
	print(mat.group(0))