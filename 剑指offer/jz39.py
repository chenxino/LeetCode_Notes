class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        T= len(nums)/2
        if len(nums) == 1:
            return nums[0]
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
                if dic[i] >= T:
                    return i
        return 