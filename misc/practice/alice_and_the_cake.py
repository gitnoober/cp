import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


# lOOKOUT FOR THE EDGE CASES

for _ in range(int(input())):
    n = int(input())
    a = sorted(maps())
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    ok = True
    for i in range(n):
        if a[i] % 2 == 0:
            # leads to two even numbers or none at all
            if d[2 * a[i]] >= 2:
                d[2 * a[i]] -= 2
            else:
                d[a[i]] -= 1
        else:
            x, y = 2 * a[i], (2 * a[i]) + 1
            if d[x] and d[y]:
                d[x] -= 1
                d[y] -= 1
            else:
                d[a[i]] -= 1
    print(d)


# 3  --- 1
# 1 2  --- 2
# 1 1 1 ---  2
# maybe by sorting

# shortest element - x
# x -> 2*x, (2*x) + 1
# 2*x -> 4*x, 2*((2*x)+1)  --- both are even
#
# 5 - > 2 , 3
