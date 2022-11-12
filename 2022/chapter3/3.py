import sys
x = pow(2, 100)
print(x)  # 1267650600228229401496703205376

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308,
# min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(sys.float_info.max)
# 1.7976931348623157e+308

print(sys.float_info.dig)  # 15

print(sys.int_info)

a = 3.141592653
b = 1.234567898
c = a*b
print(c)
d = 3141592653*1234567898
print(d)
