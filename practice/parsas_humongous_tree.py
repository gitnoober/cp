import sys
sys.setrecursionlimit(10 ** 5)

input = sys.stdin.buffer.readline


ANS = []
def solve():

    n = int(input())
    l, r = [0] * n, [0] * n
    gr = [[] for _ in range(n)]
    dp = [[0.0, 0.0] for _ in range(n)]

    for i in range(n):
        u, v = map(int, input().split())
        l[i] = u
        r[i] = v

    for i in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        gr[u].append(v)
        gr[v].append(u)

    def dfs(p, x):
        for u in gr[x]:
            if u == p:
                continue

            dfs(x, u)

        dp[p][0] += max(abs(l[p] - l[x]) + dp[x][0], abs(l[p] - r[x]) + dp[x][1])
        dp[p][1] += max(abs(r[p] - l[x]) + dp[x][0], abs(r[p] - r[x]) + dp[x][1])

    for i in gr[0]:
        dfs(0, i)

    ANS.append(int(max(dp[0][0], dp[0][1])))


tc = int(input())
while tc:
    tc -= 1
    solve()

print('\n'.join(map(str, ANS)))
