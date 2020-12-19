import math

def nth_root(val, n):
	ret = val**(1.0/n)
	#print(ret)
	return ret;

def find_y(x):
	ret = []
	temp = 1
	three_th_root = nth_root(x, 3)
	print(f'three_th_root = {three_th_root}')
	while(temp < three_th_root):
		print(f'temp = {temp}')
		temp_sum = math.pow(temp, 3) + math.pow(temp, 2) + 1
		print(f'temp = {temp}, temp_sum = {temp_sum}')
		if(temp_sum < x):
		    ret.append(temp)
		temp += 1
	# 	break
	return ret

x = 100
ret = find_y(x);
index = 0
while(index < len(ret)):
	print(ret[index])
	index += 1

# test = __builtins__.pow(3,4)
# print(test)

# import math
# test2 = math.pow(3, 4)
# print(test2)