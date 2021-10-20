class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        row = len(matrix)
        colum =len(matrix[0])
        result = []
        r_p = 0
        r_f = row-1
        c_l = 0
        c_r = colum-1
        def one_layer(u, d, l, r):
            if u>d or l>r:
                return 
            if u == d:
                for i in range(l, r+1):
                    result.append(matrix[u][i])
                return 
            if l == r:
                for i in range(u, d+1):
                    result.append(matrix[i][l])
                return 
            for i in range(l, r):
                result.append(matrix[u][i])
            for i in range(u, d):
                result.append(matrix[i][r])
            for i in range(r, l, -1):
                result.append(matrix[d][i])
            for i in range(d, u, -1):
                result.append(matrix[i][l])
            one_layer(u+1, d-1, l+1, r-1)
        one_layer(r_p, r_f, c_l, c_r)
        return result

# 大佬解法
class Solution:
    def spiralOrder(self, matrix:[[int]]) -> [int]:
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i]) # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r]) # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res
