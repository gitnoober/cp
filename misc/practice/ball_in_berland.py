import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


from collections import defaultdict

for _ in range(*maps()):
    a, b, k = maps()
    A = [*maps()]
    B = [*maps()]
    da = defaultdict(int)
    db = defaultdict(int)

    for i in range(k):
        da[A[i]] += 1
        db[B[i]] += 1

    ans = 0

    for i in range(k):
        x, y = A[i], B[i]
        ans += k - da[x] - db[y] + 1

    print(ans // 2)
