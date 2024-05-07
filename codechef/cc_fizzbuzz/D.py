# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import collections
import io
import os

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")


def solve():

    for _ in range(*linp()):
        n, k = linp()
        A = linp()
        a = []
        i = 0
        first = {}
        while i < n:
            c = A[i]
            j = i
            while i < n and c == A[i]:
                i += 1

            if c not in first:
                first[c] = j

            a.append(c)
        tot = 0
        freq = collections.defaultdict(list)

        for i in range(len(a)):
            if i + 1 < n:
                if a[i] != a[i + 1]:
                    tot += 1
            freq[a[i]].append(i)

        n = len(a)
        ans = []
        for i in range(1, k + 1):
            c = 0
            if freq[i][-1] == n - 1:
                c -= 1

            if freq[i][0] == 0:
                c -= 1

            x = n - (1 * (len(freq[i]) + c))
            # print(c, x, n, len(freq[i]), freq[i])
            print(x, c, freq[i])

            ans.append(c + x)

        print(ans)


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

    solve()
