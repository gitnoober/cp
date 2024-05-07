import collections


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges, blueEdges):
        gr = [[] for _ in range(n)]
        vis = set()

        for u, v in redEdges:
            gr[u].append((v, 0))

        for u, v in blueEdges:
            gr[u].append((v, 1))

        _ans, q, vis = [-1 for _ in range(n)], [], collections.defaultdict()
        dist = [float("inf") for _ in range(n)]
        dist[0] = 0

        for v, c in gr[0]:
            q.append((0, c ^ 1, 0))

        for node, color, dis in q:

            for child, col in gr[node]:
                if (child, node, col) in vis:
                    continue

                if color ^ 1 == col:
                    q.append((child, col, dis + 1))
                    dist[child] = min(dis + 1, dist[child])
                    vis[(child, node, col)] = True

        return [i if i != float("inf") else -1 for i in dist]


n = 3
3
redEdges = [[0, 1], [0, 2]]
blueEdges = [[1, 0]]
obj = Solution().shortestAlternatingPaths(n, redEdges, blueEdges)
print(obj)
