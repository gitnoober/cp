inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


def solve():

    for _ in range(*maps()):
        (n,) = maps()
        c = list(maps())
        a = list(maps())
        b = list(maps())
        dp = [0] * n
        for i in range(1, n):
            if i == 1:
                dp[i] = c[i] + 1 + abs(a[i] - b[i])
            else:
                if a[i] == b[i]:
                    dp[i] = c[i] + 1
                    continue

                x = (c[i] + 1) + abs(a[i] - b[i])
                y = (c[i] + 1) + (dp[i - 1] - abs(a[i] - b[i]))
                dp[i] = max(x, y)

        mx = 0
        for i in dp:
            mx = max(mx, i)
        print(mx)


if __name__ == "__main__":

    def input():
        return sys.stdin.readline().rstrip("\r\n")

    def maps():
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
