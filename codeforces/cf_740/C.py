import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


for _ in range(*maps()):
    (n,) = maps()
    p = []

    for i in range(n):
        a = [*maps()]

        N = a[0]
        st = a[1]

        for j in range(1, N + 1):
            if st + j <= a[j]:
                st += (a[j] - (st + j)) + 1

        p.append((st + 1, st + N + 1))

    p1 = sorted(p, key=lambda x: (x[0], -x[1]))

    ans, cur = p1[0]
    extra = 0

    for i in range(1, n):
        if cur < p1[i][0]:
            extra += p1[i][0] - cur

        x = p1[i][1] - p1[i][0]
        cur = max(cur, p1[i][1], cur + x)

    ans += extra

    print(ans)
