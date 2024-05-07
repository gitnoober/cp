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
H, W, C = maps()
A = [[*maps()] for _ in range(H)]
m = min(min(i) for i in A)
res = 10**18
for i in range(H):
    for j in range(W):
        a = A[i][j]
        for d in range(1, 10**6):
            if a + C * d + m > res:
                break
            for k in range(d + 1):
                if i + k >= H:
                    break
                l = d - k
                if l + j < W:
                    res = min(res, A[i + k][j + l] + C * d + a)
                if j - l > -1:
                    res = min(res, A[i + k][j - l] + C * d + a)
                if i - k > -1:
                    if j + l < W:
                        res = min(res, A[i - k][j + l] + C * d + a)
                    if j - l >= 0:
                        res = min(res, A[i - k][j - l] + C * d + a)

print(res)
# d = ((i+k) -i) - ((j+l) -j)
