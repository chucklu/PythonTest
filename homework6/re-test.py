import re
txt = '把/BA 我/PN 的/DEG 这些/DT 小/JJ 警察/NN 给/VV 吓走/VV 了/AS'
rgx_pat= r'\s+给/[A-Z]+\s+(?P<vb>[\u4e00-\u9fa5]+/V[A-Z]*)\s+'
rgx = re.compile(rgx_pat)
for mat in rgx.finditer(txt):
	print(mat.group(0))