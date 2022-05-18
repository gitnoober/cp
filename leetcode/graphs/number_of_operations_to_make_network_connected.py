class Solution:
    def makeConnected(self, n: int, connections) -> int:
        # number of connected components - 1
        if len(connections) < n - 1 :
            return - 1

        vis , gr = [False]*n , [[] for _ in range(n)]
        ans = extra_cables = 0

        for i,j in connections:
            gr[i].append(j)
            gr[j].append(i)
            
        for i in range(n):
            if vis[i]:continue

            q, cables, num_nodes, vis[i] = [i] , 0 , {i}, True
            for j in q:
                for v in gr[j]:
                    if not vis[v]:
                        q.append(v)
                        vis[v] = True

                    # cables+=1
                    num_nodes.add(v)

            # print(i, cables, num_nodes, vis)
            # cables//=2
            # extra_cables += cables - (len(num_nodes) - 1)
            ans +=1

        return ans - 1
        
        
            


n = 4
# connections = [[0,1],[0,2],[0,3],[1,2]]
connections = [[0,1],[0,2],[1,2]]
obj = Solution().makeConnected(n, connections)
print(obj)