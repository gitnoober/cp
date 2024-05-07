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
    W, H = maps()
    x1, y1, x2, y2 = maps()
    w, h = maps()
    if w + (x2 - x1) > W and h + (y2 - y1) > H:
        print(-1)
        continue
    h_, w_ = y2 - y1, x2 - x1

    ans = maxx
    if h_ + h <= H:
        ans = min(ans, h - y1, y2 - (H - h))
    if w + w_ <= W:
        ans = min(ans, w - x1, x2 - (W - w))

    print(max(0, ans))
