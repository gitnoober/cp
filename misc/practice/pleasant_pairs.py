# from math import round


def sol(n, a):
    # x = set()
    # cnt1 = 0
    # for i in range(n - 1, -1, -1):
    #     p = (i + 1) // a[i]
    #     if p in x:
    #         cnt1 += 1
    #     x.add(a[i] - p)
    # x.clear()
    # cnt2 = 0
    # for i in range(n - 1, -1, -1):
    #     p = (i + 1) // a[i]
    #     if p in x:
    #         cnt2 += 1
    #     x.add(a[i] - p)
    # return min(cnt1, cnt2)
    # return cnt


def brute(n, a):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] * a[j] == i + j + 2:
                print(a[i], a[j], i, j)
                cnt += 1
    return cnt


tc = int(input())
while tc:
    n = int(input())
    a = list(map(int, input().split()))
    ans1 = brute(n, a)
    ans2 = sol(n, a)
    if ans1 != ans2:
        print(a)
        print(ans1, ans2)
    tc -= 1
