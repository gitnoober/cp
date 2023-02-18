from collections import defaultdict


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges, blueEdges):
        edges = defaultdict(list)
        ans = [float("inf")] * n
        ans[0] = 0
        st = [(0, 0, [-1])]  # node, dis, color
        vis = {(-1, 0, -1)}
        for u, v in redEdges:
            edges[u].append((v, 1))
        for u, v in blueEdges:
            edges[u].append((v, 0))

        for node, dis, color in st:
            for adj, nxt_color in edges[node]:
                if (node, adj, nxt_color) not in vis and color != nxt_color:
                    ans[adj] = min(ans[adj], dis + 1)
                    st.append((adj, dis + 1, nxt_color))
                    vis.add((node, adj, nxt_color))

        for i in range(n):
            if ans[i] == float("inf"):
                ans[i] = -1
        return ans


n = 5
redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]]
blueEdges = [[1, 2], [2, 3], [3, 1]]
obj = Solution().shortestAlternatingPaths(n, redEdges, blueEdges)
print(obj)


"""
                                0
                            /
                        1
                    /
                2
            /
        3
    /
4
"""
