"""
Topological sort vs DFS
edge(u,v) -- u comes before v (applies to all the edges), not necessarily true for a dfs
"""


class TopologicalSort:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(self.graph)
        self.stack = []
        self.vis = [False for _ in range(self.V)]

    def dfs(self, node):
        self.vis[node] = True
        for v in self.graph[node]:
            if not self.vis[v]:
                self.dfs(v)
        self.stack.append(node)

    def topo_sort(self):
        for i in range(self.V):
            if not self.vis[i]:
                self.dfs(i)
        return self.stack[::-1]

# the vertex with no incoming edges is placed first
# Time Complexity - O(V + E)


class KhansToplogicalSort:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(self.graph)
        self.vis = [False for _ in range(self.V)]
        self.inn = [0 for _ in range(self.V)]
        self.q = []

    def calc_indegree(self):
        for i in range(self.V):
            for j in self.graph[i]:
                self.inn[j] += 1

        for i in range(self.V):
            if self.inn[i] == 0:
                self.q.append((self.inn[i], i))

    def topo_sort(self):
        stack = []
        self.calc_indegree()
        vis = set()
        for x, idx in self.q:
            for j in self.graph[idx]:
                self.inn[j] -= 1
                self.q.append((self.inn[j], j))
            if x == 0 and idx not in vis:
                stack.append(idx)
                vis.add(idx)
        return stack


if __name__ == '__main__':
    tc = int(input())
    n = int(input())
    # a = list(map(int, input().split()))
    gr = [[] for _ in range(n)]
    # for i in range(n):
    #     if a[i] == - 1:
    #         continue
    #     gr[i].append(a[i])
    for i in range(n):
        u, v = map(int, input().split())
        gr[u].append(v)

    # obj = TopologicalSort(gr)
    # print(obj.topo_sort())
    obj = KhansToplogicalSort(gr)
    print(obj.topo_sort())
