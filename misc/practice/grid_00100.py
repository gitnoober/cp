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
    n = len(arr)
    R = [sum(i) for i in arr]
    C = []

    for j in range(n):
        s = 0
        for i in range(n):
            s += arr[i][j]
        C.append(s)
    R.sort()
    C.sort()
    return (R[-1] - R[0]) ** 2 + (C[-1] - C[0]) ** 2


def solve():

    n, k = linp()
    arr = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    if k == 0 or k == n * n:
        print(0)
        val = 1 if n * n == k else 0
        for i in range(n):
            for j in range(n):
                print(val, end="")
            print()
    elif k < n:
        print(2)
        for i in range(n):
            print(*arr[i], sep="")
    else:
        arr = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        idx, c, K = 0, 1, k - n
        while K > 0:
            for i in range(n):
                tot = 0
                if arr[i][idx] == 0:
                    tot += 1
                if arr[i][(idx + c) % n] == 0:
                    tot += 1

                if K - tot >= 0:
                    arr[i][idx] = arr[i][(idx + c) % n] = 1
                    K -= tot
                elif tot == 1 and K > 0:
                    if arr[i][idx] == 0:
                        arr[i][idx] = 1
                    else:
                        arr[i][(idx + 1) % n] = 1
                    K -= 1

                idx += 1
                idx %= n

            c += 1

        print(calc(arr))
        for i in range(n):
            print(*arr[i], sep="")


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
