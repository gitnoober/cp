import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


arr = []
for i in range(1, 1700):
    if i % 3 and i % 10 != 3:
        arr.append(i)
    if len(arr) == 1000:
        break
for _ in range(*maps()):
    (k,) = maps()
    print(arr[k - 1])
