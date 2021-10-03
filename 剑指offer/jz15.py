class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = (n-1)&n
        return count