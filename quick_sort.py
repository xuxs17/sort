#快速排序
def quick_sort(list,i,j):
    if i >= j :
        return list
    pivot = list[i]
    low = i
    high = j
    while i < j:
        while i < j and list[j] >= pivot:
            j -= 1
        list[i] = list[j]
        while i < j and list[i] <= pivot:
            i += 1
        list[j] = list[i]
    list[j] = pivot
    quick_sort(list,low,i-1)
    quick_sort(list,i+1,high)
    return list

list=[30,24,5,58,18,36,12,42,39]
i = 0
j = len(list) - 1
print(quick_sort(list,0,j))
