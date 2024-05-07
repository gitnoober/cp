import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


for _ in range(*maps()):
    (n,) = maps()
    arr = [input() for _ in range(n)]
    for i in range(150):
        x = bin(i)[2:]
        x = "0" * (n - len(x)) + x
        if x not in arr:
            print(x)
            break
