import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


def solve():
    n, m = maps()
    a = [*maps()]

    if m == 1:
        print(1, 1, sep="\n")
        return

    arr = [True] * (m + 1)
    se = set()
    arr[0] = False
    for i in a:
        se.update(pf(i))

    for i in se:
        if i <= m and arr[i]:
            for j in range(i, m + 1, i):
                arr[j] = False
    arr = [i for i in range(m + 1) if i <= m and arr[i]]

    print(len(arr), *arr, sep="\n")


solve()
