class Solution:
    # 动态规划
    # 特别需要注意长度小于3的时候不分割效果会更好。
    def cuttingRope(self, n: int) -> int:
        max_products = [0, 1, 2, 3]
        if n <= 3:
            max_products = [0, 1, 1, 2]
            return max_products[n]
        for i in range(4, n+1):
            j = 1
            now_max = int(i/2)*(i-int(i/2))
            while j <= int(i/2):
                temp = max_products[j]*max_products[i-j]
                if temp > now_max:
                    now_max = temp
                j += 1
            
            max_products.append(now_max)
            print(i)
            print(max_products)
        return max_products[n]

class Solution:
    def cuttingRope(self, n: int) -> int:
        # 贪心算法
        if n <= 3:
            max_products = [0, 1, 1, 2]
            return max_products[n]
        timesOf3 = int(n/3)
        if n - timesOf3*3 == 1:
            timesOf3 -= 1
        timesOf2 = int((n - timesOf3*3)/2)
        return 3 ** timesOf3 * 2 ** timesOf2