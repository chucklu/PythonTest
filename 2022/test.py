# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

name = input("请输入姓名：")
print("你好，{0}".format(name))
print()

a, b = 0, 1
while (b < 1000):
    print(a, b)
    a, b = b, a+b
