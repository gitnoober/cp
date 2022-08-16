from collections import defaultdict

cnt = [0]


def bfs(adj, u, par, vis):
    q = [(u, par)]
    for node, parent in q:
        for child in adj[node]:
            if child == parent:
                continue
            if vis[child]:
                continue

            vis[child] = True
            cnt[0] += 1
            q.append((child, node))


N = int(input())
for _ in range(N):
    n = int(input())
    adj = [[] for _ in range(n)]
    flag = True
    for _ in range(n):
        u, v = map(lambda x: int(x) - 1, input().split())
        adj[u].append(v)
        adj[v].append(u)

    for i in adj:
        if len(i) > 2:
            flag = False
            break

    if not flag:
        print("NO")
        continue

    mark = [-1] * n
    for i in range(n):
        if mark[i] > -1:
            continue

        q = [(i, 0)]
        while len(q):
            c, m = q.pop(0)

            if mark[c] > -1:
                if m != mark[c]:
                    flag = False
                    break
                else:
                    continue
            mark[c] = m

            for v in adj[c]:
                q.append((v, 1 - m))

            if not flag:
                break
    print(["NO", "YES"][flag])
