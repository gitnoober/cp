from os import path
import sys
import time

# mod = int(1e9 + 7)
from math import factorial

# from string import ascii_lowercase ,ascii_uppercase
from bisect import *
from functools import reduce
from operator import mul

maxx = float("inf")
def I():
    return int(sys.stdin.buffer.readline())
def lint():
    return [int(x) for x in sys.stdin.buffer.readline().split()]
def S():
    return sys.stdin.readline().strip("\n")
def grid(r):
    return [lint() for i in range(r)]
localsys = 0
start_time = time.time()
# left shift --- num*(2**k) --(k - shift)
def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)


def ceill(n, x):
    return (n + x - 1) // x


T = 1


def solve():  # college_ life 4
    n, e, h, a, b, c = lint()
    ans = maxx
    for i in range(n + 1):
        if e < i or h < i:
            break
        left = n - i
        eggs = e - i
        choc = h - i
        price = i * c
        if a < b:
            k = min(left, eggs // 2)
            price += k * a
            left -= k
            if left <= choc // 3:
                price += left * b
                ans = min(ans, price)
        else:
            k = min(left, choc // 3)
            price += k * b
            left -= k
            if left <= eggs // 2:
                price += left * a
                ans = min(ans, price)
    print(-1 if ans == maxx else ans)


def run():
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")


run()
T = I() if T else 1
for _ in range(T):
    solve()


if localsys:
    print("\n\nTime Elased :", time.time() - start_time, "seconds")
