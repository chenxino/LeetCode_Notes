class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array == None:
            return False
        row = len(array)
        col = len(array[0])
        x = 0
        y = col - 1
        while x < row and y >= 0:
            if array[x][y] == target:
                return True
            elif array[x][y] > target:
                y -= 1
            elif array[x][y] < target:
                x += 1
        return False
                
                