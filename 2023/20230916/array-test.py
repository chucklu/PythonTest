def insert(nums: list[int], num: int, index: int):
    originLength=len(nums)
    print(originLength)
    tempNums=[None]*(originLength+1)
    for i in range(0,originLength+1):
        print(i)
        if i<index:
            tempNums[i] = nums[i]
        elif i==index:
            tempNums[i]=num
        else:
            tempNums[i]=nums[i-1]
    nums[:]=tempNums

nums=[1,2,4,6,7]
insert(nums,8,3)
print(nums)