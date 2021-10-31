class Solution:
    def permutation(self, s: str) -> List[str]:
        flag_s = [True]*len(s)
        print(flag_s)
        
        now_s = ''
        results = []
        def next_num(now_s, flag_s):
            print(flag_s)
            for i in range(len(s)):
                if flag_s[i] == True:
                    flag_s[i] = False
                    
                    now_s += s[i]
                    if len(now_s) == len(s):
                        if now_s not in results:
                            results.append((now_s))
                    else:
                        next_num(now_s, flag_s)
                    flag_s[i] = True
                    now_s = now_s[:-1]
        next_num(now_s, flag_s)
        return results

# 大佬解法 思想是交换元素 从前往后，依次通过交换确定每个元素位置，
class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))   # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)               # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换
        dfs(0)
        return res

