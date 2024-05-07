from os import path
import sys

# mod = int(1e9 + 7)
# import re

# from bisect import bisect_left, bisect_right
# popping from the end is less taxing,since you don't have to shift any elements
maxx = float("inf")
def I():
    return int(sys.stdin.buffer.readline())
def tup():
    return map(int, sys.stdin.buffer.readline().split())
def lint():
    return [int(x) for x in sys.stdin.buffer.readline().split()]
def S():
    return sys.stdin.readline().replace("\n", "").strip()


def grid(r, c):
    return [lint() for i in range(r)]


# def debug(*args, c=6): print('\033[3{}m'.format(c), *args, '\033[0m', file=sys.stderr)
def stpr(x):
    return sys.stdout.write(f"{x}" + "\n")
def star(x):
    return print(" ".join(map(str, x)))
if path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")

# left shift --- num*(2**k) --(k - shift)
# input = sys.stdin.readline


def gasoline():
    n = I()
    f = lint()
    c = lint()
    a = sorted(zip(c, f), key=lambda x: x[0])
    need = n
    _cnt, ans = 0, 0
    for i in range(n):
        if need > 0:
            if need > a[i][1]:
                ans += a[i][0] * a[i][1]
            else:
                ans += need * a[i][0]
            need -= a[i][1]
        else:
            break
    print(ans)
    # SORTING BY COIN VALUES


t = I()
for _ in range(t):
    gasoline()
