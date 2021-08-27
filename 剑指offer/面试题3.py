from typing import List
import math
# 寻找数组中重复数字
# 时间复杂度o(n)
def find_duplicates(nums: List[int])-> int:
    dic = {}
    for i in nums:
        if str(i) not in dic.keys():
            dic[str(i)] = 1
        else:
            return i
    return None

# 空间复杂度o(1) 
def find_duplicates2(nums: List[int])-> int:
    for i in range(len(nums)):
        if nums[i]<0 or nums[i]>len(nums):
            return None

    i = 0
    def swap(i,j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    while i<len(nums):
        if i != nums[i]:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                swap(i, nums[i])
        else:
            i += 1
    return None
print(find_duplicates2([2,3,1,0,2,5,3,10]))

# 不改变原数组，找出长度为n+1重复数字。时间复杂度o(nlogn),空间复杂度o(1)
def find_dupliate3(nums: List[int])->int:
    if len(nums) == 0:
        return None
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = math.floor((start+end)/2)
        count = 0
        for i in range(len(nums)):
            if nums[i] >= start and nums[i] <= mid:
                count += 1
            
        if end == start:
            if count>1:
                return start
            else:
                break
        if count > mid-start+1:
            end = mid
        else:
            start = mid
    return -1
    