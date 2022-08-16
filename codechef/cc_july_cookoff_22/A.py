for _ in range(int(input())):
    n = int(input())
    if n == 3:
        print(-1)
        continue

    ans = []
    x = 1
    while len(ans) < n:
        ans.append(x)
        ans.append(x + 1)
        x += 3

    print(*ans[:n])
