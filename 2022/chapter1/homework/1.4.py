# 计算1+2!+3!+……+10！
sum = 0
temp = 1
for i in range(1, 11):
    temp = temp*i
    sum = sum+temp
print("运算结果是：{}".format(sum))
