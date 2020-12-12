import re
year_pattern = r'(?P<year>\d{4})年'
month_pattern = r'(?P<month>\d{1,2})月'
day_pattern = r'(?P<day>\d{1,2})日'
patterns_dic = {'year':year_pattern, 'month':month_pattern, 'day':day_pattern}
txt = '他出生在2020年3月。'
for key in patterns_dic:
	mat = re.search(patterns_dic[key], txt)
	print(mat)
	if mat:
		print(f'{mat.group(key)}')