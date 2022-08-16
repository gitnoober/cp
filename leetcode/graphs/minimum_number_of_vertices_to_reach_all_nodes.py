
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        inn = [0 for _ in range(n)]
        gr = [[] for _ in range(n)]
        for u,v in edges:
            inn[v]+=1
            gr[u].append(v)

        q = []
        for i in range(n):
            if inn[i] == 0 :
                q.append(i)
        return q





n = 6
# edges = [[1,3],[2,0],[2,3],[1,0],[4,1],[0,3]]
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
obj = Solution().findSmallestSetOfVertices(n, edges)
print(obj)
