from os import path
import sys
import time

mod = int(1e9 + 7)
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


def solve():
    # calculate the row prefix and column prefix
    # then calculate the sum of each sqaure and check if it's average is greater than or equal to x
    # the biggest square it can form is min(n,m), min(n,m)
    n, m, k = lint()
    arr = [[0] * (m + 1)]
    for _ in range(n):
        arr.append([0] + lint())
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            arr[i][j] += arr[i][j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            arr[j][i] += arr[j - 1][i]
    min(n, m)
    ans = 0
    for i in range(1, n + 1):
        st = i
        en = m
        while st >= 1 and st <= n and en >= 1 and en <= m:
            if (
                arr[st][en] - arr[st - i][en] - arr[st][en - i] + arr[st - i][en - i]
            ) // (i * i) >= k:
                ans += n - st + 1
                en -= 1
            else:
                st += 1
    print(ans)


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
