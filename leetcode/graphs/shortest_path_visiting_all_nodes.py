import collections

class Solution:
    def shortestPathLength(self, graph):
        # all paths
        # self.n = len(graph)
        # gr = [set() for _ in range(self.n)]

        # for i in range(self.n):
        #     for j in graph[i]:
        #         gr[i].add(j)
        #         gr[j].add(i)

        # self.mx = float('inf')
        # self.cnt = 0
        # self.dic = {}
        # self.seee = set()

        # def dfs(unique_nodes, path, par, node):
        #     # print(unique_nodes, path, par, node, gr[node], "oo")
        #     # print(node, path, )
        #     self.cnt+=1

        #     if len(unique_nodes) == self.n:
        #         if len(path) < self.mx:
        #             self.mx = len(path)

        #     if len(path) >= 2*self.n or len(path) > self.mx:
        #         return

        #     for v in gr[node]:

        #         dfs(unique_nodes | {v}, path+[v], node, v)

        # for i in range(self.n):
        #     dfs({i}, [i], -1, i)

        # print(self.cnt)
        # return self.mx - 1

        def bfs():
            n = len(graph)

            masks = [1<<i for i in range(n)]
            q = collections.deque((i, masks[i]) for i in range(n))
            allvis = (1<<n)  - 1

            allstates = [{masks[i]} for i in range(n)]

            steps = 0
            while q :
                cnt = len(q)
                while cnt :
                    node, state = q.popleft()
                    if state == allvis:
                        return steps

                    for child in graph[node]:
                        new_state = state | masks[child]

                        if new_state == allvis:
                            return steps + 1

                        if new_state not in allstates[child]:
                            allstates[child].add(new_state)
                            q.append((child, new_state))

                    cnt-=1

                steps+=1

            return float('inf')
        return bfs()
        # print(bfs())








graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
obj = Solution().shortestPathLength(graph)