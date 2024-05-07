from itertools import combinations
from math import ceil
import sys


k = int(input())
n = int(input())
g = int(input())

x = ceil(k / n)
a = list(range(n)) * x


def check(arr):
    for i in range(k - 1):
        for j in range(i + 1, min(k, i + g + 1)):
            if arr[j] == arr[i]:
                return False
    return True


# check([1,2])
cnt = 0
for i in combinations(a, k):
    if check(i):
        cnt += 1
# print(cnt)
sys.stdout.write(str(cnt))
