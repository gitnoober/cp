import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


s = input()
print("AC" if s == "Hello,World!" else "WA")
