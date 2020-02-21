#冒泡排序
def bubbleSort(nums):
    for i in range(len(nums) - 1): # 遍历 len(nums)-1 次
        for j in range(len(nums) - i - 1): # 已排好序的部分不用再次遍历
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] # Python 交换两个数不用中间变量
    return nums

a = [1,3,5,76,8,9,4,2,434,5432]
print(bubbleSort(a))