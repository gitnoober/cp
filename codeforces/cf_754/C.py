inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


def naive(s):
    n = len(s)
    ans = inf
    for i in range(n):
        for j in range(i, n + 1):
            x = s[i:j]
            a, b, c = x.count("a"), x.count("b"), x.count("c")
            if a > b and a > c and len(x) > 1:
                ans = min(ans, len(x))
                # if len(x) == 3:
                #     print(x)
    return ans


def solve():
    for _ in range(*maps()):
        (n,) = maps()
        s = input()
        ans = inf
        for i in range(n):
            ca = cb = cc = 0
            for j in range(i, i + 7):
                if j == n:
                    break
                if s[j] == "a":
                    ca += 1
                elif s[j] == "b":
                    cb += 1
                else:
                    cc += 1
                if ca > cb and ca > cc and (j - i) >= 1:
                    ans = min(ans, j - i + 1)
        # print(ans)

        if ans == inf:
            ans = -1
        print(ans)


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
