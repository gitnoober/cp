def solve():
    n, m = map(int, input().split())
    a = input()
    b = input()
    # if a == b:
    #     return "YES"

    # if n <= m:
    #     return "NO"

    # c1 = 0
    # c0 = 0
    # for i in a:
    #     if i == "1":
    #         c1 += 1
    #     else:
    #         c0 += 1

    # cc0, cc1 = 0, 0
    # for i in b:
    #     if i == "1":
    #         cc1 += 1
    #     else:
    #         cc0 += 1

    # if c0 >= cc0 and c1 >= cc1:
    #     return "YES"
    # return "NO"
    # print(a[: n - m + 1], a[-m + 1])
    # if a[-m + 1 :] == b[1:] and b[0] in a[: n - m + 1]:
    #     return "YES"
    # return "NO"
    i = n - 1
    j = m - 1
    ok = True
    while i > 0 and j > 0:
        if a[i] == b[j]:
            i -= 1
            j -= 1
        else:
            ok = False
            break
    if j == 0 and ok:
        while i >= 0 and j >= 0:
            if a[i] == b[j]:
                i -= 1
                j -= 1
            else:
                i -= 1
    if ok and j == -1:
        return "YES"
    else:
        return "NO"


N = int(input())
for _ in range(N):
    ans = solve()
    print(ans)
