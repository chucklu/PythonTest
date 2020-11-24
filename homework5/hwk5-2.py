#2. 设计一个函数，功能为给定一个Unicode字符串，将字符串中每个字符和它对应的Unicode码值（Code Point）以十进制方式打印出来。
def show_unicode_code_points(txt):
	for ch in txt:
		code_point = ord(ch)
		print(f"{ch} {code_point}")

txt = "hello world"
show_unicode_code_points(txt)