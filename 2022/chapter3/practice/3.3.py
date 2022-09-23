import decimal
x = -77.
print(type(x))
y = decimal.Decimal(x)
print("-77. is {:.2e}".format(y))

x = 4.3e-3
print("4.3e-3 is {}".format(x))
