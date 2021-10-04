class Solution:
    def myPow(self, x: float, n: int) -> float:
        def simple_pow(base, exp):
            if exp == 0:
                return 1
            temp = simple_pow(base, exp>>1)
            if exp&1 == 1:
                return temp*temp*base
            else:
                return temp*temp
        if x == 0 and n < 0:
            # 出现错误
            return 0
        flag_n = False
        if n < 0:
            flag_n = True
            n = -n
        result = simple_pow(x, n)
        if flag_n:
            result = 1/result
        return result