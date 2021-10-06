# 考虑大数，自己写的垃圾解法
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        nums = []
        def trans(s):
            result = 0
            for i in s:
                result = result*10 + int(i)
            return result
        def get_number(ss, nn, ii):
            if ii == nn:
                nums.append(trans(ss))
                return 
            for i in range(10):
                ss[ii] = str(i)
                get_number(ss, nn, ii+1)
        num_str = ['0']*n
        for i in range(10):
            num_str[0] = str(i)
            get_number(num_str, n, 1)
        return nums[1:]

class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(s)
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1
        
        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return ','.join(res)

