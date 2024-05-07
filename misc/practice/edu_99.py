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


def seqofswaps():
    for _ in range(I()):
        n, x = tup()
        ls = lint()
        cnt = 0
        for i in range(n):
            if ls == sorted(ls):
                break
            if ls[i] > x:
                ls[i], x = x, ls[i]
                cnt += 1
        if ls == sorted(ls):
            print(cnt)
        else:
            print(-1)


def jump():
    a = []
    c = 0
    for i in range(1, 1500):
        c += i
        a.append(c)
    for _ in range(I()):
        n = I()
        x = bisect_left(a, n)
        if a[x] - n == 1:
            print(x + 2)
        else:
            if a[x] == n:
                print(x + 1)
                continue
            print(x + 1)
