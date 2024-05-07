from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        time = 1
        n = len(edges)
        node_time = [0] * n
        ans = -1
        for i in range(n):
            if node_time[i] > 0:
                continue
            start = time
            node = i
            while node != -1 and node_time[node] == 0:
                node_time[node] = time
                time += 1
                node = edges[node]

            if node != -1 and node_time[node] >= start:
                ans = max(ans, time - node_time[node])
        return ans


edges = [3, 3, 4, 2, 3]
# edges = [2,-1,3,1]
edges = [3, 4, 0, 2, -1, 2]
edges = [3, 3, 4, 2, 3]
obj = Solution().longestCycle(edges)
print(obj)


"""
0 --> 3

1 --> 4

2 --> 0  --> 3 ---> 2


0 --> 3 --> 2 --> 4 --> 3
1 --> 3 --> 2 --> 4 --> 3






"""
