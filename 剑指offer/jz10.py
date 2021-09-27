import sys

i = sys.maxsize

class Solution:
    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        ll = [0, 1]
        if n<2:
            return ll[n]
        fib1 = 0
        fib2 = 1
        fibb = 0
        for i in range(n-1):
            fibb = fib1 + fib2
            fib1 = fib2
            fib2 = fibb
        return fibb%MOD
print(Solution().fib(45))