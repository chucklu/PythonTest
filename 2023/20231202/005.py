def bubbleSort(nums):
    for j in range(len(nums)-1,0,-1):
        for i in range(j):
            #print(i)
            if(nums[i]>nums[i+1]):
                nums[i],nums[i+1]=nums[i+1],nums[i]

nums=[9,3,5,4,10]
bubbleSort(nums)
print(nums)

nums2= [64, 34, 25, 12, 22, 11, 90]
bubbleSort(nums2)
print(nums2)