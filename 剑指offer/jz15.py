class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = (n-1)&n
        return count
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        flag = 1
        for i in range(32):
            if n & flag:
                count += 1
            flag = flag << 1
        return count