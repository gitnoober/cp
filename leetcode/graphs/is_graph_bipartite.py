
class Solution:
    def isBipartite(self, graph: int) -> bool:
        n = len(graph)
        color  = [-1 for i in range(n)]

        def dfs(node, col):
            color[node] = col
            for child in graph[node]:
                if color[child] == -1 and not dfs(child, col^1):
                    return False

                if color[child] == col:
                    return False

            return True



        for i in range(n):
            if color[i] == -1 and not dfs(i,0):
                return False
        return True








graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
obj = Solution().isBipartite(graph)
print(obj)