# lOOKOUT FOR THE EDGE CASES

from math import sqrt
from bisect import bisect_left

pr = []


def sol():
    n = int(input())
    idx = bisect_left(pr, n)
    gr = [[] for _ in range(n)]
    ans = [None] * n
    vis = [False] * n
    inn = [0] * n

    for x in range(idx - 10, idx + 10):
        if x >= len(pr) or x < 0:
            continue
        val = pr[x]
        for i in range(n):
            v = val - i
            if v < 0 or v >= n:
                continue
            gr[i].append(v)
            inn[i] += 1

    print(gr)
    q = [i for i in range(n) if inn[i] == 1]
    for i in q:
        for node in gr[i]:
            ans[i] = node
            vis[node] = True
    print(ans)
    # print(inn, "Q")
    # for node in q:
    #     # inn[node] -= 1
    #     # vis[node] = True
    #     for neighbour in gr[node]:
    #         inn[neighbour] -= 1
    # print(inn)

    return [-1]


N = 100001
for i in range(int(sqrt(N)) + 5):
    x = int(sqrt(i))
    if (x * x) == i:
        pr.append(i)

# print(pr[:10])
tc = int(input())
while tc:
    x = sol()
    print(*x)
    tc -= 1
