rate = 6.0
TempStr = input("请输入带有符号的金额: ")
if TempStr[-1] in ['￥']:
    dollar = (eval(TempStr[0:-1]))/rate
    print("转换后的美元是{:.2f}$".format(dollar))
elif TempStr[-1] in ['$']:
    yuan = rate*eval(TempStr[0:-1])
    print("转换后的人民币是{:.2f}￥".format(yuan))
else:
    print("输入格式错误")