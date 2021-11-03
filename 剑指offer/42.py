class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = float('-inf')
        for i in nums:
            s += i
            if s>m:
                m = s
            if s<0:
                s = 0
        return m