from os import path
import sys

maxx, localsys, mod = float("inf"), 0, int(1e9 + 7)
if path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
input = sys.stdin.readline

"""
PROBLEM - A
for _ in range(int(input())):
    n = int(input())
    print(math.ceil(((2**n) -1 ) /2 ))"""
