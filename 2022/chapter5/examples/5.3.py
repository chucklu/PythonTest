def reverse(s):
    print("s = {}".format(s))
    if s == "":
        return s
    else:
        temp = s[1:]  # 等价于s[1:len(s)]
        print("temp = {}".format(temp))
        temp2 = reverse(temp)+s[0]
        print("temp2 = {}".format(temp2))
        return temp2

str = input("请输入一个字符串：")
print(reverse(str))
