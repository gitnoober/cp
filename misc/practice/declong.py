from os import path
import sys

# mod = int(1e9 + 7)
# import re
from math import log2

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


def power(x):
    if x == 0:
        return 1
    return 1 << int(log2(x))


def main():
    n, k = tup()
    ls = lint()
    i = 0
    while k > 0 and i < n - 1:
        k -= 1
        flag = 0
        p = power(ls[i])
        ls[i] ^= p
        for j in range(i + 1, n):
            if ls[j] ^ p < ls[j]:
                ls[j] ^= p
                flag = 1
                break
        if flag == 0:
            ls[n - 1] = ls[n - 1] ^ p
        while i < n and ls[i] == 0:
            i += 1

    if n < 3 and k % 2:
        ls[n - 1], ls[n - 2] = ls[n - 1] ^ 1, ls[n - 2] ^ 1
    else:
        if k == 1:
            ls[n - 1], ls[n - 2] = ls[n - 1] ^ 1, ls[n - 2]

    print(" ".join(map(str, ls)))


for _ in range(I()):
    main()


def stropers():
    for _ in range(I()):
        s = S()
        n, d = len(s), set()
        for i in range(n):
            ones = odd = even = 0
            for j in range(i, n):
                if s[j] == "1":
                    ones += 1
                else:
                    if ones % 2:
                        odd += 1
                        # 1's before zeroes
                    else:
                        even += 1
                # unique strings such that the number of ones are different and so is the kength
                d.add((j - i, even, odd))
        print(len(d))
