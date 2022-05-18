from collections import deque


for _ in range(int(input())):
    n, k = map(int, input().split())

    def c(a):
        return a ^ (n - 1)

    ans = []
    vis = set()
    if k == 0:
        for i in range(n):
            if i not in vis and c(i) not in vis:
                vis.add(c(i))
                vis.add(i)
                ans.append([i, c(i)])
    elif 0 < k < n - 1:
        ans.append([0, c(k)])
        ans.append([n - 1, k])
        vis |= {0, k, c(k), n - 1}
        for i in range(n):
            if i not in vis and c(i) not in vis:
                vis.add(c(i))
                vis.add(i)
                ans.append([i, c(i)])
    else:
        if n >= 8:
            ans.append([n - 2, n - 1])
            ans.append([1, 3])
            vis |= {1, 3, n - 2, n - 1}
            for i in range(n):
                if i not in vis and c(i) not in vis:
                    vis.add(c(i))
                    vis.add(i)
                    ans.append([i, c(i)])
            p = [i for i in range(n) if i not in vis]
            for i in range(0, len(p), 2):
                ans.append([p[i], p[i + 1]])
        else:
            print(-1)
    [print(*i) for i in ans]
