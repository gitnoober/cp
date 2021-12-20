

def maximumDetonation(bombs):

    def check(p1, p2):
        x1, y1, r1 = p1
        x2, y2, r2 = p2
        return r1 * r1 >= ((x2 - x1)**2) + ((y2 - y1)**2)

    n = len(bombs)
    gr = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if check(bombs[i], bombs[j]):
                gr[i] += [j]

    def BFS(start):
        vis = set()
        q = [start]
        vis.add(start)
        res = 0

        for x in q:
            for v in gr[x]:
                if v in vis:
                    continue

                q.append(v)
                vis.add(v)

        return len(vis)

    ans = 1
    for i in range(n):
        ans = max(ans, BFS(i))
    return ans


bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
x = maximumDetonation(bombs)
print(x)
