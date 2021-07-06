from collections import defaultdict
class Solution:
    def displayTable(self, orders):
        dic = {}
        tableIds = []
        foodIds = [] 
        for record in orders:
            if record[1] not in dic.keys():
                dic[record[1]] = defaultdict(int)
            dic[record[1]][record[2]] += 1
            if int(record[1]) not in tableIds:
                tableIds.append(int(record[1])) 
            if record[2] not in foodIds:
                foodIds.append(record[2])
        foodIds = sorted(foodIds)
        tableIds = sorted(tableIds)
        out = []
        out.append(foodIds)

        for i in tableIds:
            print([str(i)]+[str(dic[str(i)][j]) for j in foodIds])
            out.append([str(i)]+[str(dic[str(i)][j]) for j in foodIds])
        return out

# 大佬的 作者：AC_OIer
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        ans = []
        # 桌号 : {餐品 : 个数}（用于构造内容）
        tm = defaultdict(lambda: defaultdict(int))
        # 餐品（用于构造 title）
        ts = set()
        for c,t,f in orders:
            tidx = int(t)
            ts.add(f)
            tm[tidx][f] += 1
        n, m = len(tm) + 1, len(ts) + 1
        # 构造 title & 手动排序
        foods = sorted(ts)
        title = []
        title.append("Table")
        title += foods
        ans.append(title)
        # 构造内容 & 手动排序
        for tidx in sorted(tm.keys()):
            cur = []
            cur.append(str(tidx))
            for food in foods:
                cur.append(str(tm[tidx][food]))
            ans.append(cur)
        return ans



print(Solution().displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
        