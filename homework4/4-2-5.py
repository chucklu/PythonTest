
#assume you hava 5 elements in list [5,1,4,2,8]
#loop1
#[5,1,4,2,8]-->[8,1,4,2,5] find biggest is 8, swap 8 and the first element 5
#loop2, skip first element 8, and find biggest in left 4 elements
#[8,1,4,2,5]-->[8,5,4,2,1] find biggest is 5, swap 5 and the second element
#loop3, skip first two elements, and find biggest in left 3 elements
#[8,5,4,2,1]-->[8,5,4,2,1] find biggest is 4, swap 4 and the third element, they are the same elements, no need to change

def sort_nums(data_list):
	#print(data_list)
	count = len(data_list)
	for i in range(count-1):
		tuple_item = find_max(i,data_list)
		max_number_index = tuple_item[0]
		max_number = tuple_item[1]
		#print(f"loop{i+1}, max_number_index = {max_number_index}, max_number = {max_number}")
		if(i != max_number_index):
			temp = data_list[i]
			data_list[i] = data_list[max_number_index]
			data_list[max_number_index] = temp
		#print(f"loop{i+1} {data_list}")
	return data_list

def find_max(start_index,data_list):
	#print(f"start_index = {start_index}")
	count = len(data_list)
	max_number = data_list[start_index]
	max_number_index = start_index
	for i in range(start_index+1,count):
		#print(f"i = {i}")
		if(max_number < data_list[i]):
			max_number = data_list[i]
			max_number_index = i
	return (max_number_index,max_number)
data_list = [9, 23, 10, 217, 11, 23, 55, 79, 196, 224, 56, 135]
#data_list = [5,1,4,2,8]
result = sort_nums(data_list)
print(result)