import os
import sys
import collections as c

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
nCr, ceil = (
    lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r),
    lambda n, x: (n + x - 1) // x,
)
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


def check(s, d, H, M):
    h, m = "", ""
    for i in range(4):
        if s[i] not in d:
            return "-1"
        else:
            if i <= 1:
                h += d[s[i]]
            else:
                m += d[s[i]]
    P = (h + m)[::-1]
    h = P[0] + P[1]
    m = P[2] + P[3]
    return (
        s[0] + s[1] + ":" + s[2] + s[3] if 0 <= int(h) < H and 0 <= int(m) < M else "-1"
    )


for _ in range(int(input())):
    h, m = maps()
    sh, sm = input().rstrip("\n").split(":")
    d = {"0": "0", "1": "1", "2": "5", "5": "2", "8": "8"}
    if check(sh + sm, d, h, m) != "-1":
        print(sh + ":" + sm)
        continue
    c, H, M, mn1, t1 = 0, int(sh), int(sm), None, [0, 0]
    while c < h + 2:
        x = ""
        x, cnt = x + "0" + str(H) if len(str(H)) == 1 else str(H), 0
        while cnt < m:
            y = ""
            y += "0" + str(M) if len(str(M)) == 1 else str(M)
            if check(x + y, d, h, m) != "-1":
                P = x + ":" + y
                mn1, t1 = P, [c, cnt]
                break
            M = (M + 1) % m
            cnt += 1
            if M == 0:
                break
        if mn1:
            break
        H = (H + 1) % h
        c += 1
    print(mn1)
