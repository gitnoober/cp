from collections import defaultdict

import math
import os
import random
import re
import sys

#
# Complete the 'vanity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING_ARRAY numbers
#


def convert(a, d):
    res = []
    for i in a:
        i = i.lower()
        if i not in d:
            continue
        res.append(str(d[i]))

    return "".join(res)


def subArray(arr, n):
    subs = set()

    for i in range(n):
        for j in range(i + 1, n + 1):
            subs.add(arr[i : j + 1])
    return subs


def vanity(codes, numbers):
    d = {
        "a": 2,
        "b": 2,
        "c": 2,
        "d": 3,
        "e": 3,
        "f": 3,
        "g": 4,
        "h": 4,
        "i": 4,
        "j": 5,
        "k": 5,
        "l": 5,
        "m": 6,
        "n": 6,
        "o": 6,
        "p": 7,
        "q": 7,
        "r": 7,
        "s": 7,
        "t": 8,
        "u": 8,
        "v": 8,
        "w": 9,
        "x": 9,
        "y": 9,
        "z": 9,
    }

    ans = set()
    subs = defaultdict(set)
    for i in numbers:
        s = subArray(i, len(i))
        for es in s:
            subs[es].add(i)

    for i in range(len(codes)):
        res = convert(codes[i], d)
        if res in subs:
            for k in subs[res]:
                ans.add(k)
    return sorted(ans)


n = int(input())
codes = [input() for _ in range(n)]
m = int(input())
numbers = [input()[1:] for _ in range(m)]
print(vanity(codes, numbers))
