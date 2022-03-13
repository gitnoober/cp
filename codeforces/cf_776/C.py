import heapq

for _ in range(int(input())):
    input()
    n, m = map(int, input().split())
    # A = []
    h = []
    for __ in range(m):
        x, w = map(int, input().split())
        heapq.heappush(h, [w, x, __])

    res = []
    ans = 0
    while len(res) < 2 * n:
        x = heapq.heappop(h)
        ans += x[0]
        res.append(x)

    res.sort(key=lambda x: x[1])
    print(ans)
    i = 0
    j = len(res) - 1
    arr = []
    while i < j:
        arr.append((res[i][-1] + 1, res[j][-1] + 1))
        i += 1
        j -= 1
    [print(*i) for i in arr]
    print()
