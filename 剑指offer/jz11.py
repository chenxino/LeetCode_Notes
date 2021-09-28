# 快排
import random
print(list(range(1,3)))
def partition(nums, start, end):
    def Swap(a, b):
        nums[a], nums[b] = nums[b], nums[a]
    if nums == []:
        return start
    index = random.randint(start, end)
    Swap(index, end)
    small = start - 1
    for i in range(start, end):
        if nums[i]<nums[end]:
            small += 1
            if small != i:
                Swap(small, i)
    small += 1
    Swap(small, end)
    return small

def quick_sort(num_list, start, end):
    if len(num_list) == 0:
        return []
    index = partition(num_list, start, end)
    if index>start:
        quick_sort(num_list, start, index-1)
    if index<end:
        quick_sort(num_list, index+1, end)
    return num_list
    
print(quick_sort([3,2,0,5], 0, 3))

# 最小数 对旋转数还有一种二分查找的方法，但要考虑三点相同和旋转0的情况
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if numbers == []:
            return 
        min_nums = numbers[0]
        for i in numbers:
            if i < min_nums:
                min_nums = i
        return min_nums


