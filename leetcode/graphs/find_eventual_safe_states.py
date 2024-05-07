class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        out = [0] * n

        q = []
        grp = [[] for _ in range(n)]
        for i in range(n):
            out[i] = len(graph[i])
            if out[i] == 0:
                q.append(i)

            for j in graph[i]:
                grp[j].append(i)

        for i in q:
            for v in grp[i]:
                out[v] -= 1
                if out[v] == 0:
                    q.append(v)
        q.sort()
        return q

        # for i in range(n):
        #     print(i, grp[i])


graph = [[], [0, 2, 3, 4], [3], [4], []]
obj = Solution().eventualSafeNodes(graph)
