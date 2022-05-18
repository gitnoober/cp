

class Solution:
    def minReorder(self, n: int, connections):
        changed = 0
        gr = [[] for _ in range(n)]
        edges = set()
        for u,v in connections:
            gr[u].append(v)
            gr[v].append(u)
            edges.add((u,v))

        def dfs(u,p):
            nonlocal changed
            changed += (p,u) in edges
            for v in gr[u]:
                if v == p:
                    continue
                dfs(v,u)

        dfs(0,-1)
        return changed





"""
all paths converge to 0
go to the 

"""
n = 5
connections = [[1,0],[1,2],[2,3],[4,2]]
obj = Solution().minReorder(n,connections)
print(obj)