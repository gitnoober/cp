from heapq import heappop, heappush
from bisect import bisect_right

N = int(input())
for _ in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    sub = []
    for i in range(n):
        if a[i] < i + 1:
            sub.append((a[i], i + 1))
    sub.sort()
    # print(sub)
    ans = 0
    for i in range(len(sub)):
        p = (sub[i][1], float("inf"))
        idx = bisect_right(sub, p)
        # print(idx)
        if idx != len(sub):
            ans += len(sub) - idx
    print(ans)
