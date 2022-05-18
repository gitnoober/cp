

# class Solution:
#     def findCircleNum(self, isConnected):
#         n = len(isConnected)
#         par = [i for i in range(n)]

#         def find(u):
#             ucopy = u
#             while par[u] != u :
#                 u = par[u]

#             while par[ucopy] != ucopy:
#                 par[ucopy], ucopy = u, par[ucopy]

#             return u

#         def union(u,v):
#             u,v = find(u), find(v)

#             if u != v :
#                 par[v] = u

#         for i in range(n):
#             for j in range(n):
#                 if isConnected[i][j]:
#                     union(i, j)

#         vis = set()
#         for i in range(n):
#             vis.add(find(i))

#         return len(vis)





class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        gr = [[] for _ in range(n)]
        vis = set()

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    gr[i].append(j)

        cnt = 0 
        for i in range(n):
            if i in vis:
                continue

            def dfs(i):
                vis.add(i)
                for j in gr[i]:
                    if j in vis:
                        continue
                    dfs(j)
            dfs(i)
            cnt+=1

        return cnt


# disjoint set union
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
obj = Solution().findCircleNum(isConnected)
print(obj)


