import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


from itertools import permutations

s, k = input().split()
k = int(k)

arr = set()
for i in permutations(s, len(s)):
    arr.add("".join(i))
arr = sorted(arr)
print(arr[k - 1])
