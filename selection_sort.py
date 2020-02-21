#选择排序
def selection_sort(nums):
    for i in range(len(nums)):
        min_num = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_num]:
                min_num = j
            nums[min_num],nums[i] = nums[i],nums[min_num]
    return nums

a = [5,3,2,6,8,1]
print(selection_sort(a))


