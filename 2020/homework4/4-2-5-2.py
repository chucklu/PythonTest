#Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, 
#compares adjacent elements and swaps them if they are in the wrong order.

#assume you hava 5 elements in list [5,1,4,2,8]
#descending order need to compare the last two elements first
#loop1
#[5,1,4,2,8]-->[5,1,4,8,2] compare element at index3 and element at index4, 2<8(not descending order), swap them
#[5,1,4,8,2]-->[5,1,8,4,2] compare element at index2 and element at index3, 4<8, swap them
#[5,1,8,4,2]-->[5,8,1,4,2] compare element at index1 and element at index2, 1<8, swap them
#[5,8,1,4,2]-->[8,5,1,4,2] compare element at index0 and element at index1, 5<8, swap them
#loop2, skip the element at index0
#[8,5,1,4,2]-->[8,5,1,4,2] compare element at index3 and element at index4, 4>2(descending order), no need to swap
#[8,5,1,4,2]-->[8,5,4,1,2] compare element at index2 and element at index3, 1<4(not descending order), swap them
#[8,5,4,1,2]-->[8,5,4,1,2] compare element at index1 and element at index2, 5>4(descending order), no need to swap
#loop3, skip the element at index0 and index1
#[8,5,4,1,2]-->[8,5,4,2,1] compare element at index3 and element at index4, 1<2(not descending order), swap them
#[8,5,4,2,1]-->[8,5,4,2,1] compare element at index2 and element at index3, 4>2(descending order), no need to sap them
#loop4, skip the element at index0 and index1 and index2
#[8,5,4,2,1]-->[8,5,4,2,1] compare element at index3 and element at index4, 2>1(descending order), no need to sap them
	
def sort_nums(data_list):
	count =  len(data_list)
	for j in range(0, count):
		swapped = False
		for i in range(count-1, j,-1):
			#print(f"loop{j+1}, i-1={i-1}, i={i}")
			if(data_list[i-1]<data_list[i]):
				data_list[i-1], data_list[i] = data_list[i], data_list[i-1]
				swapped = True
			#print(data_list)
		if(swapped == False):
			break
		#print(f"loop{j+1}, {data_list}")
	return data_list

data_list = [9, 23, 10, 217, 11, 23, 55, 79, 196, 224, 56, 135]
#data_list = [5,1,4,2,8]
#data_list = [11, 23, 10, 217, 9, 23, 55, 79, 196, 224, 56, 135]
result = sort_nums(data_list)
print(result)