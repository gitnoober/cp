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
def ok(a):
    return True if sorted(a) == a or sorted(a) == a[::-1] else False


for _ in range(int(input())):
    n = int(input())
    a = list(maps())
    ans = n + n - 1
    for i in range(n - 2):
        if not ok(a[i : i + 3]):
            ans += 1
    for i in range(n - 3):
        bool = True
        for j in range(i, i + 4):
            t = []
            for k in range(i, i + 4):
                if j != k:
                    t.append(a[k])
            if ok(t):
                bool = False
                break
        if bool:
            ans += 1
    print(ans)
