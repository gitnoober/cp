import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


from _collections import deque

mod = int(1e9 + 7)

n, m = maps()
gr = [[] for _ in range(n)]
for _ in range(m):
    u, v = maps()
    u -= 1
    v -= 1

    gr[u].append(v)
    gr[v].append(u)


st = deque([0])
dis = [None] * n
cnt = [0] * n
dis[0] = 0
cnt[0] = 1

while st:
    x = st.popleft()

    for v in gr[x]:

        if dis[v] is None:
            dis[v] = dis[x] + 1
            cnt[v] = cnt[x]
            st.append(v)

        elif dis[v] == dis[x] + 1:
            cnt[v] += cnt[x]
            cnt[v] %= mod


# print(dis, cnt, sep='\n')
print(cnt[-1])
