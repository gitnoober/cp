import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    p[find(x)] = find(y)


n, m1, m2 = maps()

p = [i for i in range(2 * n + 1)]

for i in range(m1):
    u, v = maps()
    union(u, v)


for i in range(m2):
    u, v = maps()
    union(u + n, v + n)


ans = []

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if find(i) != find(j) and find(i + n) != find(j + n):
            """
            if i , j belong to diff components in both forests then you can merge them , also one merge won't harm
            other merges because each tree(component) is independent.
            """
            ans.append((i, j))
            union(i, j)
            union(i + n, j + n)

print(len(ans))
[print(*i) for i in ans]
