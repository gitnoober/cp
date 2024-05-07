# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
# mod = int(1e9) + 7
# mod = 998244353


def solve():

    n, q = linp()
    s = list(input())
    cnt = 0
    for i in range(2, n):
        if s[i - 2] == "a" and s[i - 1] == "b" and s[i] == "c":
            cnt += 1

    for i in range(q):
        x = input().split()
        idx = int(x[0]) - 1

        a = []
        for j in range(max(0, idx - 2), min(n, idx + 3)):
            a.append(s[j])

        t = [0, 0]
        # t = []
        for tt in range(2):
            og = 0
            for j in range(len(a)):
                if (
                    j + 2 < len(a)
                    and a[j] == "a"
                    and a[j + 1] == "b"
                    and a[j + 2] == "c"
                ):
                    og += 1

            # t.append(og)
            t[tt] = og
            s[idx] = x[1]
            a = []
            for j in range(max(0, idx - 2), min(n, idx + 3)):
                a.append(s[j])

        cnt -= t[0]
        cnt += t[1]
        print(cnt)


if __name__ == "__main__":
    # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

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
