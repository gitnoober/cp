class DetectCycle:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(self.graph)
        self.color = [0 for _ in range(self.V)]

    def dfs(self, node):
        """
        returns True if there is a cycle else False
        Basically finds a back edge (points to an ancestor)
        """

        self.color[node] = 1
        for v in self.graph[node]:
            if self.color[v] == 1: # if found a node already processed, then this is the back edge
                return True

            if self.color[v] == 0 and self.dfs(v) is True: # unprocessed so send it back to the dfs
                return True

        self.color[node] = 2
        return False

    def is_cycle(self):
        for i in range(self.V):
            if self.color[i] == 0 and self.dfs(i):
                print(i)
                return True
        return False


# graph = [[] for _ in range(5)]
# obj = DetectCycle(graph)
# print(obj)

if __name__ == '__main__':
    tc = int(input())
    n = int(input())
    graph = [[] for _ in range(n)]
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] == - 1:
            continue
        graph[i].append(a[i])

    obj = DetectCycle(graph)
    print(obj.is_cycle())
