import re
txt = 'I#have##a###cat.'
rgx_pat = r'#+'
txt_new, count = re.subn(rgx_pat, '\t', txt)
print(txt_new)
print(count)