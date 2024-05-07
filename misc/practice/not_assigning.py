def bfs(node, ok, par):
    vis = [False] * len(gr)
    vis[par] = vis[node] = True
    q = [(node, ok)]

    for u, val in q:
        for v, e in gr[u]:
            if not vis[v]:
                vis[v] = True
                ans[e] = val ^ 1
                q.append((v, ans[e]))


if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        inn = [0] * (n + 1)
        gr = [[] for _ in range(n + 1)]

        for _ in range(n - 1):
            u, v = map(int, input().split())
            inn[u] += 1
            inn[v] += 1
            gr[u].append((v, _))
            gr[v].append((u, _))

        fl = 0
        for i in range(n + 1):
            if inn[i] >= 3:
                fl = 1
                break

        if fl:
            print(-1)
            continue

        ans = [0 for i in range(n - 1)]
        cur, prev, ok, a = 1, None, 0, [2, 5]
        while len(gr[cur]) != 1:
            cur += 1
        for p in range(n - 1):
            for v, e in gr[cur]:
                if v != prev:
                    ans[e] = a[ok ^ 1]
                    ok ^= 1
                    cur, prev = v, cur
                    break
        print(*ans)
