class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n =len(graph)
        color = [0]*n

        def safe(x):
            if color[x]>0:
                return color[x] == 2
            color[x]=1
            for y in graph[x]:
                if not safe(y):
                    return False
            color[x] = 2
            return True
        return [i for i in range(n) if safe(i)]


# 拓扑排序
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rg = [[] for _ in graph]
        for x, ys in enumerate(graph):
            for y in ys:
                rg[y].append(x)
        in_deg = [len(ys) for ys in graph]

        q = deque([i for i, d in enumerate(in_deg) if d == 0])
        while q:
            for x in rg[q.popleft()]:
                in_deg[x] -= 1
                if in_deg[x] == 0:
                    q.append(x)

        return [i for i, d in enumerate(in_deg) if d == 0]