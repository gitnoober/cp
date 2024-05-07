import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


for _ in range(*maps()):
    a, b, c = maps()
    x = abs(a - b)
    if a <= 2 * x and b <= 2 * x and c <= 2 * x:
        if c <= x:
            if c + x <= 2 * x:
                print(c + x)
            else:
                print(-1)
        else:
            if c - x >= 0:
                print(c - x)
            else:
                print(-1)

    else:
        print(-1)
