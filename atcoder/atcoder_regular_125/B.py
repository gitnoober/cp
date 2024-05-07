import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


def sol1():
    (n,) = maps()
    i = 1
    ans = 0
    while i * i <= n:
        x = n // i
        ans += (x - i + 2) // 2
        i += 1
    print(ans % 998244353)
