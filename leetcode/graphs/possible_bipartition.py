
class Solution:
    def possibleBipartition(self, n: int, dislikes) -> bool:
        q = []
        gr = [[] for _ in range(n)]
        color = [-1 for i in range(n)]
        for u, v in dislikes:
            u,v=u-1,v-1
            gr[u].append(v)
            gr[v].append(u)


        ok  = True

        def dfs(node, col):
            color[node] = col
            for child in gr[node]:
                if color[child] == col:
                    return False
                elif color[child] == -1 and not dfs(child, col^ 1):
                    return False

            return True


        for i in range(n):
            if color[i] == -1 and not dfs(i, 0):
                ok = False

        return ok





n = 4
dislikes = [[1,2],[1,3],[2,4]]
obj = Solution().possibleBipartition(n, dislikes)
print(obj)


