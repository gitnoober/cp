import os
import sys

maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)
def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
def ceil(n, x):
    return (n + x - 1) // x
osi, oso = (
    "/home/priyanshu/Documents/cp/input.txt",
    "/home/priyanshu/Documents/cp/output.txt",
)
if os.path.exists(osi):
    sys.stdin = open(osi, "r")
    sys.stdout = open(oso, "w")

input = sys.stdin.readline


def maps():
    return map(int, input().split())


# THINK ABOUT THE EDGE CASES ..........
for _ in range(int(input())):
    n, x, y = maps()
    if n == 2:
        print(x, y)
        continue
    last = maxx
    for d in range(51):
        for X in range(51):
            for Y in range(51):
                a1 = x - X * d
                a11 = y - Y * d
                if a1 == a11 and a1 > 0:
                    t = a1 + (n - 1) * d
                    if t >= y and t < last:
                        last, A, D = t, a1, d
    ans = [A]
    for i in range(1, n):
        ans.append(ans[-1] + D)
    print(*ans)
