import math

def nth_root(val, n):
	ret = val**(1.0/n)
	return ret;

def find_y(x):
	ret = []
	temp = 1
	three_th_root = nth_root(x, 3)
	while(temp < three_th_root):
		temp_ret = math.pow(temp, 3) + math.pow(temp, 2) + 1
		print(f'temp = {temp}, temp_ret = {temp_ret}')
		if(temp_ret < x):
			ret.append(temp)
		temp += 1
	return ret

x = 100
ret = find_y(x);
index = 0
while(index < len(ret)):
	print(ret[index])

# test = __builtins__.pow(3,4)
# print(test)

# import math
# test2 = math.pow(3, 4)
# print(test2)