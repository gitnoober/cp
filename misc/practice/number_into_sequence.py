import os
import sys
import math

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
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


# think about the edge cases

for _ in range(int(input())):
    n = int(input())
    m = n
    mx = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        tp = 0
        while n % i == 0:
            n //= i
            tp += 1
        if tp > mx:
            mx = tp
            x = i
    print(mx)
    for i in range(mx - 1):
        m //= x
        print(x, end=" ")
    print(m)
