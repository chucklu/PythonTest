import re
txt = 'I#have##a###cat.'
rgx_pat = r'\s*#+\s*'
words = re.split(rgx_pat, txt)
print(words)