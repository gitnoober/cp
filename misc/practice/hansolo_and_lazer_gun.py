import os
import sys
import math as mt
import operator as op
import functools as fn

maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)
def nCr(n, r):
    return fn.reduce(op.mul, range(n - r + 1, n + 1), 1) // mt.factorial(r)

def ceil(a, b):
    return (a + b - 1) // b

def lcm(a, b):
    return a * b // mt.gcd(a, b)

def gcdm(*args):
    return reduce(mt.gcd, args, 0)

def lcm(a, b):
    return a * b // mt.gcd(a, b)

def lcmm(*args):
    return reduce(lcm, args, 1)


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


#   THINK ABOUT THE EDGE CASES ..........

#   DON'T SUBMIT UNLESS YOU ARE ABSOLUTELY SURE !!!!!

n, x0, y0 = maps()
dic = {}
for _ in range(n):
    X, Y = maps()
    if y0 - Y == 0:
        dic["-1"] = 1
    else:
        dic[(X - x0) / (Y - y0)] = 1
print(len(dic.keys()))

"""
the number of slopes would have sufficed , first solution would have been right but i forgot that the slope
is to be calculated with respect to the gun not stupidly calculating with other points.
"""
