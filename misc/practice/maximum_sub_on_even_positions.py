# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import io
import os

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
# mod = int(1e9) + 7
# mod = 998244353


def calc(arr):
    x = [0, 0]
    for i in range(len(arr)):
        x[i % 2] += arr[i]
    return x[0]


def naive(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            t = arr[:i] + arr[i:j][::-1] + arr[j:]
            c = calc(t)
            # if c == 37:
            #     print(c, t, arr[i:j])
            ans = max(ans, c)
    return ans


def kadane(arr):
    curr = 0
    mx = 0
    for i in arr:
        curr += i
        mx = max(mx, curr)
        # if curr < 0:
        #     curr = 0
    return mx


def solve():

    (n,) = linp()
    a = list(linp())
    tot = 0
    for i in range(n):
        if i % 2 == 0:
            tot += a[i]

    mx_sum = 0
    curr = 0
    for i in range(0, n - (n % 2), 2):
        curr = max(0, curr + a[i + 1] - a[i])
        mx_sum = max(curr, mx_sum)
    curr = 0
    for i in range(1, n - (n % 2 == 0), 2):
        curr = max(0, curr + a[i] - a[i + 1])
        mx_sum = max(mx_sum, curr)

    print(tot + mx_sum)


if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    def linp():
        return [int(i) for i in input().split()]

    logging.basicConfig(
        format="%(message)s",
        level=logging.WARNING,
    )
    logger = getLogger(__name__)
    logger.setLevel(logging.INFO)

    def debug(msg, *args):
        logger.info(f"{msg}={pprint.pformat(args)}")

    for _ in range(*linp()):
        solve()
