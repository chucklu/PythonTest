import re
txt = 'I#have##a###cat.'
rgx_pat = r'#+'
words = re.split(rgx_pat, txt)
print(words)