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
# t = 26
# ans =['' , '']
# st = list('bcdefghijklmnopqrstuvwxyz')
# while t:
# 	t-=1
# 	x = st.pop(0)
# 	N = 26 - len(st)
# 	for i in ans:


# print(st)
# for i in ans:
# 	print(i)
for _ in range(int(input())):
    s = list(input().rstrip("\n"))
    if "a" not in s:
        print("NO")
        continue
    if len(s) == 1 and "a" in s:
        print("YES")
        continue
    idx = s.index("a")
    s.pop(idx)
    st = "abcdefghijklmnopqrstuvwxyz"
    c = 1
    ok = True

    while s:
        if idx < len(s) and s[idx] == st[c]:
            s.pop(idx)
            c += 1
        elif idx - 1 > -1 and s[idx - 1] == st[c]:
            s.pop(idx - 1)
            idx -= 1
            c += 1
        else:
            ok = False
            break
    print("YES") if ok else print("NO")
