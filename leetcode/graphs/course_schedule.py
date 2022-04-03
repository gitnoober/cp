class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        inn = [0] * numCourses
        gr = [[] for _ in range(numCourses)]
        gra = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            gr[b].append(a)  # can go from b to a
            gra[a].append(b)
            inn[a] += 1
        q = []
        for i in range(numCourses):
            if not inn[i]:
                q.append(i)

        vis = set(q)

        for i in q:
            for j in gr[i]:
                if j in vis:
                    continue
                ok = True
                for k in gra[j]:
                    if k not in vis:
                        ok = False
                if ok:
                    q.append(j)
                    vis.add(j)

        return True if len(vis) == numCourses else False


# numCourses = 5
# prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
numCourses = 3
prerequisites = [[1, 0], [1, 2], [0, 1]]
obj = Solution().canFinish(numCourses, prerequisites)
print(obj)
