import sys
from itertools import combinations
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


# lOOKOUT FOR THE EDGE CASES


def cnt(n):
    c = 0
    for i in range(64, -1, -1):
        if (1 << i) & n:
            c += 1
    return c


def main():
    arr = [1]
    mul = 1
    sums = defaultdict(set)

    for i in range(2, 100):
        mul *= i
        if mul > 10**12:
            break
    arr.append(mul)

    for i in range(1, len(arr) + 1):
        for j in combinations(arr, i):
            sums[i].add(sum(j))
    sums[0].add(0)

    for _ in range(int(input())):
        n = int(input())
        ans = float("inf")
        for j in sums:
            for i in sums[j]:
                if i <= n:
                    ans = min(ans, j + cnt(n - i))
        print(ans)


main()
