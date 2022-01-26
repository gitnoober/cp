import sys
import heapq as hp


def input():
    return sys.stdin.readline().rstrip("\r\n")


# from collections import defaultdict


def sol1():
    n = int(input())
    maxLen = 0
    minL = float('inf')
    maxR = 0
    minC = float('inf')
    v1 = v2 = None
    for _ in range(n):
        l, r, val = map(int, input().split())

        if l < minL:
            minL = l
            v1 = val
            minC += v1

        if r > maxR:
            maxR = r
            v2 = val
            minC += v2

        if l == minL:
            v1 = min(v1, val)

        if r == maxR:
            v2 = min(v2, val)

        if r - l + 1 > maxLen:
            minC = val
            maxLen = r - l + 1

        if r - l + 1 == maxR - minL + 1:
            minC = min(minC, val)

        ans = v1 + v2
        if maxLen == maxR - minL + 1:  # for single segment
            ans = min(ans, minC)

        print(ans)


def sol2():
    n = int(input())
    heap1, heap2 = [], []
    hp.heapify(heap1)
    hp.heapify(heap2)

    for _ in range(n):
        l, r, val = map(int, input().split())
        hp.heappush(heap1, (l, val, _))
        hp.heappush(heap2, (-r, val, _))

        x, y = hp.heappop(heap1), hp.heappop(heap2)
        minl = x[0]
        maxr = -y[0]
        minC = x[-1] + y[-1]
        if r - l + 1 == maxr - minl + 1:
            minC = min(minC, val)
        print(minC)
        hp.heappush(heap1, (l, val, _))
        hp.heappush(heap2, (-r, val, _))


tc = int(input())
while tc:
    tc -= 1
    sol1()
