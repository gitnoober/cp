N = int(input())
for _ in range(N):
    n = int(input())
    vis = set()
    ans = 0
    for i in input():
        if i in vis:
            ans += 1
        else:
            ans += 2
        vis.add(i)
    print(ans)
