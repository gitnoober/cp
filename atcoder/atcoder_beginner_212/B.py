import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


def check(ar):
    ok = True
    for i in range(1, 4):
        if (a[i - 1] + 1) % 10 != a[i]:
            ok = False
    return ok


a = list(map(int, input()))
if len(set(a)) == 1:
    print("Weak")
    exit()
if check(a):
    print("Weak")
else:
    print("Strong")
