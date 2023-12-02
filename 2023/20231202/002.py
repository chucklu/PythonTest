#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
#你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#你可以按任意顺序返回答案。
def find(nums,target):
    for i in range(len(nums)):
        a = nums[i]
        b = target-a
        for j in range(len(nums)):
            if(j==i):
                continue
            else:
                if(b==nums[j]):
                    return (i,j)
    return

nums1 = [2,7,11,15]
target1 = 9
result = find(nums1,target1)
print(result)

nums2 = [3,2,4]
target2 = 6
result = find(nums2,target2)
print(result)

nums3 = [3,3]
target3 = 6
result = find(nums3,target3)
print(result)