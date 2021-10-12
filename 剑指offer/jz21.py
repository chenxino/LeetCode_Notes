class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i<j:
            while i<j and nums[i]%2 == 1:
                i += 1
            while i<j and nums[j]%2 == 0:
                j -= 1
            if i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        return nums