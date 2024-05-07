import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


mod = 998244353


n, m, k = maps()
dp = [0] * n
nxtdp = [0] * n
gr = [[] for _ in range(n)]

for _ in range(m):
    u, v = maps()
    u -= 1
    v -= 1
    gr[u].append(v)
    gr[v].append(u)


# dp[i] -- the number of paths that end at i

# at every level nxtdp[i] = dp[i] - (j belongs to adj[i]) dp[j]

dp[0] = 1

for _ in range(k):

    s = sum(dp)

    for i in range(n):
        nxtdp[i] = s - dp[i]

        for j in gr[i]:
            nxtdp[i] -= dp[j]

        nxtdp[i] %= mod

    for i in range(n):
        dp[i] = nxtdp[i]

print(dp[0])


"""
all the vertices  of  prevdp[i] can lead to the current i , so all those path(sum of the paths) - dp[i](except their own path),
can lead to nxtdp[i]

eliminate all the broken paths , that do not lead to i
"""
