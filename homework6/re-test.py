import re
rgx_pat_phone_no = r'^((13\d)(\d{8}))'
txt = '13312345679'
mat = re.fullmatch(rgx_pat_phone_no, txt)
print(mat)
if mat:
	for i in range(0,4):
		print(f'group({i}) = {mat.group(i)}')