class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        matrix = [[0]*n for i in range(m)]

        def count_sum(x, y):
            ss = str(x)+str(y)
            s_sum = 0
            for i in ss:
                s_sum += int(i)
            return s_sum
        def dfs(x, y, l):
            if not 0 <= x < m or not 0 <= y < n:
                return l
            if matrix[x][y] == 1 or count_sum(x, y) > k:
                return l
            matrix[x][y] = 1
            l += 1
            l = dfs(x, y+1, l)
            l = dfs(x+1, y, l)
            l = dfs(x, y-1, l)
            l = dfs(x-1, y, l)
            return l
        now_l = dfs(0, 0, 0)
        print(now_l)

        return now_l