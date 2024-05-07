import os
import sys

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
nCr, ceil = (
    lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r),
    lambda n, x: (n + x - 1) // x,
)
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
    n = int(input())
    s = input().strip("\n")
    cnt = s.count("0")
    (
        print("BOB" if cnt % 2 == 0 or n <= 2 or cnt == 1 else "ALICE")
        if s == s[::-1]
        else (
            print("DRAW") if cnt == 2 and s[n // 2] == "0" and n % 2 else print("ALICE")
        )
    )

"""
So , the gist is that Alice will make the string non-palindromic so that she could use the reverse operation but at the same time
Bob will make the string palindromic and at the last operation when there is only one zero , then Bob will use the reverse operation
it is only possible for Alice to win if the number of zeroes are odd because then she could force Bob to make the last convert operation while herself using the reverse operation.
"""

"""
A.py
ans = (1 << log2(n)) - 1
closest power of 2 minus 1 to eliminate all the ones
"""
