import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


# from collections import defaultdict , deque , Counter
from math import ceil, floor

for _ in range(*maps()):
    a, b = maps()
    ans = set()

    # if Alice serves first
    p = ceil((a + b) / 2)
    q = floor((a + b) / 2)

    # if Borys serves first
    p1 = floor((a + b) / 2)
    q1 = ceil((a + b) / 2)

    for x in range(a + b + 1):
        y = a - (p - x)
        if (p - x) + y == a and y >= 0 and y <= q and x >= 0 and x <= p:
            ans.add(x + y)

        y = a - (p1 - x)
        if (p1 - x) + y == a and y >= 0 and y <= q1 and x >= 0 and x <= p1:
            ans.add(x + y)

    print(len(ans))

    for i in ans:
        print(i, end=" ")
    print()
