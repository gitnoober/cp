import os
import sys
import collections
import math

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
from functools import reduce


def maps():
    return map(int, input().split())


# THINK ABOUT THE EDGE CASES ..........


def div(n):
    se = collections.defaultdict(int)
    while n % 2 == 0:
        n //= 2
        se[2] += 1
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            se[i] += 1
            n //= i
    if n > 1:
        se[n] += 1
    return se


f = math.factorial


def sol1():
    int(input())
    ans = []
    s = [*map(int, input().rstrip("\n"))]
    p = []
    for i in s:
        x = div(f(i))
        for j in x:
            while x[j]:
                p.append(j)
                x[j] -= 1
    p = collections.Counter(p)
    OK = True
    while OK:
        for i in range(9, -1, -1):
            if p[i]:
                ok = True
                for j in range(i - 1, 1, -1):
                    if j == 4 and p[2] >= 2:
                        continue
                    elif j == 6 and p[3] and p[2]:
                        continue
                    elif j == 8 and (p[4] >= 2 and p[2] >= 3):
                        continue
                    elif j == 9 and p[3] >= 2:
                        continue
                    elif not p[j]:
                        ok = False
                if ok:
                    for j in range(i - 1, 1, -1):
                        if j == 4 and p[2] >= 2:
                            p[2] -= 2
                        elif j == 6 and p[3] and p[2]:
                            p[3] -= 1
                            p[2] -= 1
                        elif j == 8 and p[2] >= 3:
                            p[2] -= 3
                        elif j == 9 and p[3] >= 2:
                            p[3] -= 2
                        else:
                            p[j] -= 1
                    ans.append(i)
                    p[i] -= 1
                    break
        else:
            break
    print(*ans, sep="")


def sol2():
    int(input())
    a = input().rstrip("\n")
    d = ["", "", "2", "3", "322", "5", "53", "7", "7222", "7332"]
    ans = ""
    for i in a:
        ans += d[int(i)]
    print("".join(sorted(ans)[::-1]))


sol2()
