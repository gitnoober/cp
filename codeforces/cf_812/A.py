# lOOKOUT FOR THE EDGE CASES


def sol():
    n = int(input())
    xa = []
    ya = []

    for __ in range(n):
        x, y = map(int, input().split())
        xa.append(x)
        ya.append(y)

    xa.sort()
    ya.sort()

    ans = 0
    ok = False
    if xa[0] < 0 and xa[-1] > 0:
        ans += abs(xa[0]) + abs(xa[-1])

    if ya[0] < 0 and ya[-1] > 0:
        ans += abs(ya[0]) + abs(ya[-1])

    if xa[-1] <= 0 and not (xa[0] < 0 and xa[-1] > 0):
        ans += abs(xa[0])

    elif xa[0] >= 0 and not (xa[0] < 0 and xa[-1] > 0):
        ans += xa[-1]

    if ya[-1] <= 0 and not (ya[0] < 0 and ya[-1] > 0):
        ans += abs(ya[0])

    elif ya[0] >= 0 and not (ya[0] < 0 and ya[-1] > 0):
        ans += ya[-1]
    # print(xa, ya, "xxx")
    return ans * 2


tc = int(input())
while tc:
    print(sol())
    tc -= 1
