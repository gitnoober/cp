"""
mandatory conditions :
atleast 1 '1' needs to be there
"""

from collections import defaultdict
import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


# lOOKOUT FOR THE EDGE CASES

for _ in range(int(input())):
    n = int(input())
    s = input()
    cnt = [0, 0]
    dic = defaultdict(list)
    for idx, i in enumerate(s):
        cnt[int(i)] += 1
        dic[int(i)].append(idx)
    if not cnt[1] or cnt[1] % 2:
        print("NO")
    else:
        print("YES")
        edges = []
        for j in dic[0]:
            edges.append((j, (j + 1) % n))

        b = (dic[1][0] + 1) % n
        edges += [(b, (dic[1][j] + 1) % n) for j in range(1, len(dic[1]))]
        for i, j in edges:
            print(i + 1, j + 1)
