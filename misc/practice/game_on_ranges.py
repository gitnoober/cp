from collections import defaultdict, deque
for _ in range(int(input())):
    n = int(input())
    d = defaultdict(list)
    for __ in range(n):
        u, v = map(int, input().split())
        d[u].append((u, v))

    ans = []
    for i in d:
        d[i] = deque(sorted(d[i], key=lambda x: -x[1]))

    # print(d)
    for i in range(1, n + 1):
        while len(d[i]) > 0:
            pick = d[i][0]
            if len(d[i]) > 1:
                ans.append((pick[0], pick[1], d[i][1][1] + 1))
            else:
                ans.append((pick[0], pick[1], pick[0]))
            d[i].popleft()

    # print(d)
    for i in ans:
        print(*i)
