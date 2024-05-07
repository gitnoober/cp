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


#   THINK ABOUT THE EDGE CASES ..........

#   DON'T SUBMIT UNLESS YOU ARE ABSOLUTELY SURE !!!!!

for _ in range(*maps()):
    (n,) = maps()
    a = [i for i in input().rstrip("\n")]
    b = [i for i in input().rstrip("\n")]
    if "1" not in b:
        print(0)
        continue
    ans = 0
    for i in range(n):
        if a[i] == "0" and b[i] == "1":
            b[i] = a[i] = "-1"
            ans += 1
        elif a[i] == "1":
            if i - 1 >= 0 and b[i - 1] == "1":
                ans += 1
                b[i - 1] = a[i] = "-1"
            elif i + 1 < n and b[i + 1] == "1":
                ans += 1
                b[i + 1] = a[i] = "-1"
    print(ans)
