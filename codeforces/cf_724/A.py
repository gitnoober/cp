import os
import sys
import collections as c

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
def ceil(n, x):
    return (n + x - 1) // x
osi, oso = (
    "/home/priyanshu/Documents/sublimetextproject/input.txt",
    "/home/priyanshu/Documents/sublimetextproject/output.txt",
)
if os.path.exists(osi):
    sys.stdin = open(osi, "r")
    sys.stdout = open(oso, "w")

input = sys.stdin.readline


def maps():
    return map(int, input().split())


for _ in range(int(input())):
    n = int(input())
    a = list(maps())
    d = c.defaultdict(int)
    for i in a:
        d[i] += 1
    i = 0
    while i < len(a) and len(a) < 300:
        for j in range(len(a)):
            if j != i:
                x = abs(a[i] - a[j])
                if not d[x]:
                    d[x] += 1
                    a.append(x)
                if len(a) > 300:
                    break
        i += 1
    if len(a) > 300:
        print("no")
        continue
    ok = True
    for i in a:
        for j in a:
            x = abs(i - j)
            if x and not d[x]:
                print("no")
                ok = False
                break
        if not ok:
            break
    else:
        print("yes", len(a), sep="\n")
        print(*a)
