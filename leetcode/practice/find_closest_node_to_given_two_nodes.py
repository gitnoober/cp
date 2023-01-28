from collections import defaultdict


class Solution:
    def closestMeetingNode(self, edges, node1: int, node2: int) -> int:
        n = len(edges)
        reach_one = [-1] * n
        reach_two = [-1] * n
        tree = defaultdict(list)
        for i in range(n):
            if edges[i] == -1:
                continue
            tree[i].append(edges[i])

        def bfs(node, reach):
            stack = [(node, 0)]
            vis = {node}
            reach[node] = 0
            for node, dis in stack:
                for nei in tree[node]:
                    if nei in vis:
                        continue
                    reach[nei] = dis + 1
                    stack.append((nei, reach[nei]))
                    vis.add(nei)

        bfs(node1, reach_one)
        bfs(node2, reach_two)

        print(reach_one)
        print(reach_two)

        ans = float("inf")
        node = -1
        for i in range(n):
            # if i in [node1, node2]:
            #     continue
            if reach_one[i] != -1 and reach_two[i] != -1:
                x = max(reach_one[i], reach_two[i])
                if x < ans:
                    ans = x
                    node = i
        return node


# edges = [2, 2, 3, -1]
# node1 = 0
# node2 = 1


edges = [1, 2, -1]
node1 = 0
node2 = 2

obj = Solution().closestMeetingNode(edges, node1, node2)
print(obj)


"""
0 --> 1 --> 2
"""
