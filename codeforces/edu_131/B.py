N = int(input())
for _ in range(N):
    n = int(input())
    # ans = [1]
    ans = [1]
    vis = [False] * (n + 1)
    vis[0] = True
    # vis[1] = True
    for i in range(2, n + 1):
        if vis[i]:
            continue
        j = i
        while j <= n:
            ans.append(j)
            vis[j] = True
            j *= 2
    # print(ans)
    print(2)
    print(*ans)
