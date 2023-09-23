def findSmallestIndex(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallestIndex(arr)
        smallest = arr.pop(smallest_index)
        newArr.append(smallest)
    return newArr


my_list = [5, 3, 6, 2, 10]
newArr = selectionSort(my_list)
print(newArr)
