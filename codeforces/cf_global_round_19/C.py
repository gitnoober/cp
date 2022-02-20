from collections import deque
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ev, od = 0, 0
    ok = True
    for i in range(1, n - 1):
        if a[i] % 2:
            od += 1
        else:
            ev += 1

        if od > ev:
            ok = False

    # print(ok)
    if not ok:
        print(-1)
    else:
        ans = 0
        od = deque(i for i in range(n) if a[i] % 2)
        # print(od)

        for i in range(1, n - 1):
            if a[i] % 2 == 0 and od:
                ans += 1
                a[0] += 1
                a[i] -= 2
                a[od.popleft()] += 1
        # print(a)
        for i in range(1, n - 1):
            ans += a[i] // 2
        print(ans)
