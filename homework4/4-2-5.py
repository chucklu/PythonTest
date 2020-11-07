
#assume you hava 4 items in list, you will need 3 loop to finish the bubble sort
#first loop
#compare index 0 with index 1, and swap the bigger to index 0
#compare index 0 with index 2, and swap the bigger to index 0
#compare index 0 with index 3, and swap the bigger to index 0
#when first loop finishes, the item at index 1 would be the biggest, 
#then we only need to compare the left 3 items at index 1, index 2 and index 3

#second loop
#compare index 1 with index 2, and swap the bigger to index 1
#compare index 1 with index 3, and swap the bigger to index 1

#third loop
#compare index 2 with index 3, and swap the bigger to index 2

def sort_nums(data_list):
	count = len(data_list)
	#print(f"count = {count}")
	second = 1
	for i in range(count - 1):
		#print(f"loop{i + 1}")
		for j in range(second, count):
			#print(f"i = {i}, j = {j}")
			if(data_list[i] < data_list[j]):
				temp = data_list[i]
				data_list[i] = data_list[j]
				data_list[j] = temp
		second = second + 1
		#print(data_list)
	return data_list

data_list = [9, 23, 10, 217, 11, 23, 55, 79, 196, 224, 56, 135]
result = sort_nums(data_list)
print(result)