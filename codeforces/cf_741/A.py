import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps(): return [int(i) for i in input().split()]


from math import ceil

for _ in range(*maps()):
    l, r = maps()

    print(r % max(r // 2 + 1, l))
