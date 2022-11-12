# https://realpython.com/python-strings/
s = "foobar"
print("{}的字符串长度为{}".format(s, len(s)))
print(s[2:5])  # oba  从2开始，长度为5-2

print(s[:4])  # foob 省略第一个参数，第一参数就是0
print(s[0:4])

print(s[2:])  # obar 省略第二个参数，第二个参数就是字符串的长度
print(s[2:len(s)])
