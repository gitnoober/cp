
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        
        res = []
        vis = set()
        gr = [[] for _ in range(n)]
        for u,v in edges:
            gr[u].append(v)

        temp = set()
        def dfs(u):
            vis.add(u)
            temp.add(u)
            for v in gr[u]:
                if v in temp:
                    continue
                dfs(v)

        for i in range(n):
            dfs(i)
            temp.add(i)
            res.append((temp.copy(),i))
            temp.clear()

        print(res)
        res.sort(key=lambda x : -len(x[0]))
        init = set()
        # print(res)
        ans = []
        for i,j in res:
            init |= i
            ans.append(j)
            if len(init) == n:
                return  ans




n = 5
edges = [[1,3],[2,0],[2,3],[1,0],[4,1],[0,3]]
obj = Solution().findSmallestSetOfVertices(n, edges)
print(obj)
        