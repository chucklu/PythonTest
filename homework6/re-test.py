import re
txt = 'ab,a\nb'
rgx_pat = r'a.{0,4}b'
mat = re.search(rgx_pat, txt)
print(mat)
mat_str = mat.group()
print(mat_str)