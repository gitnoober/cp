import os
import sys

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
def ceil(n, x):
    return (n + x - 1) // x
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


for _ in range(int(input())):
    s = list(input().rstrip("\n"))
    n = len(s)
    for i in range(n - 1):
        if s[i] == s[i + 1] and s[i] != "-1":
            s[i + 1] = "-1"
        if i + 2 < n and s[i] == s[i + 2] and s[i] != "-1":
            s[i + 2] = "-1"
    print(s.count("-1"))
"""
Every palindrome with length greater than 3 consists of substring - palindromes of lenght 2 and 3 and if we can make then not-palindromic
we can destroy every palindromic substring of that palindrome
"""
