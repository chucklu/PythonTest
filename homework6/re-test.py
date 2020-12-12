import re
txt = 'I#have##a###cat.'
rgx_pat = r'#+'
txt_new = re.sub(rgx_pat, '\t', txt)
print(txt_new)