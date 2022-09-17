# 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print("{}*{}={:2} ".format(j, i, i*j), end=' ')
    print()
