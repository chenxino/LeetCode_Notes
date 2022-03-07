import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        self.flag = [[True]*n for i in range(n)]
        self.result = [['.']*n for i in range(n)]
        print(self.result)
        self.all_result = []
        self.n = n
        def update(x, y):
            l, r = y-1, y+1
            for i in range(x+1, self.n):
                self.flag[i][y] = False
                if l>=0:
                    self.flag[i][l] = False
                    l -= 1
                if r<n:
                    self.flag[i][r] = False
                    r += 1
            return self.flag

        def backtrack(number):
            if number == self.n:
                self.new_result = []
                for one in self.result:
                    self.new_result.append(''.join(one))
                self.all_result.append(self.new_result)
                return 
            
            for i in range(self.n):
                # print(number, i)
                # print(self.flag)
                if self.flag[number][i]:
                    self.result[number][i]='Q'
                    temp = copy.deepcopy(self.flag)
                    self.flag = update(number, i)
                    backtrack(number+1)
                    self.flag = temp
                    self.result[number][i]='.'
        backtrack(0)

        return self.all_result
        

            