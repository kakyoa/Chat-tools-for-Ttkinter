
def bubbleSort(nums):
    for i in range(len(nums)-1):    
        for j in range(len(nums)-i-1): 
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [1,12,11,14,5,6,7]
print(type(nums))
print(bubbleSort(nums))
