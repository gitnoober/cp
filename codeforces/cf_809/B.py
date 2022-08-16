from collections import defaultdict

N = int(input())
for _ in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(list)
    for i in range(n):
        d[a[i]].append(i + 1)
    res = [0] * n
    for c in d:
        if not len(d[c]):
            res[c - 1] = 0
            continue
        tot = 1
        for i in range(1, len(d[c])):
            if (d[c][i] - d[c][i - 1] - 1) % 2:
                continue
            tot += 1
        res[c - 1] = tot
    print(*res)
