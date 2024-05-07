inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger
import collections
import bisect

# sys.setrecursionlimit(10 ** 9)


def solve():
    maxN = 10**5 + 6
    prf = [[] for _ in range(maxN)]
    pr = [True] * maxN
    pr[0] = pr[1] = False
    cnt = collections.defaultdict(list)
    cnt[1].append(1)

    for i in range(maxN):
        if pr[i]:
            for j in range(2 * i, maxN, i):
                pr[j] = False

            for j in range(i, maxN, i):
                prf[j].append(i)

        cnt[len(prf[i])].append(i)

    (tc,) = maps()
    while tc:
        tc -= 1
        a, b, k = maps()
        if cnt[k][0] > b:
            print(0)
            continue

        l = bisect.bisect_right(cnt[k], a - 1)
        r = max(0, bisect.bisect_right(cnt[k], b) - 1)
        ans = r - l + 1
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
