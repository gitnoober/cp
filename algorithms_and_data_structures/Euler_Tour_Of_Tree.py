maxN = int(2e6)
idx = 0
euler_path = [-1] * maxN
vis = [0] * maxN


def euler_tree(u):
    global idx
    euler_path[idx] = u
    vis[u] = 1
    idx += 1

    for v in gr[u]:
        if vis[v] == 0:
            euler_tree(v)
            euler_path[idx] = u  # after leaving the node
            idx += 1


n = 4
gr = [[] for _ in range(n)]
gr[0].append(1)
gr[0].append(2)
gr[2].append(3)
euler_tree(0)
print(euler_path[:10])
