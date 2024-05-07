inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger
import os

# sys.setrecursionlimit(10 ** 9)


def main():
    osi = "/home/ps/Documents/cp/input.txt"
    oso = "/home/ps/Documents/cp/output.txt"
    if os.path.exists(osi):
        sys.stdin = open(osi, "r")
        sys.stdout = open(oso, "w")


def solve():

    for __ in range(*maps()):
        k, x = maps()
        tot = k * k
        if tot <= x:
            print(2 * k - 1)
        else:
            # print("lets c" ,)
            # first half
            # calculating number of messages
            ans = -1

            l, h = 1, 10**20
            while l <= h:
                m = (l + h) >> 1
                if m > 2 * k - 1:
                    h = m - 1
                    continue

                if m <= k:
                    t = m * (m + 1) // 2
                else:
                    res = m - k
                    if res == k - 1:
                        t = k * k
                    else:
                        t = m * (m + 1) // 2
                        res2 = (2 * k - 1) - m
                        (k - 1) * (k) // 2
                        g = res2 * (res2 + 1) // 2
                        t = tot - g
                        # print(t , m ,tot)
                if t <= x:

                    ans = m + (1 if (x - t) > 0 else 0)
                    l = m + 1
                else:
                    h = m - 1

                    # counting from last
            print(ans)


if __name__ == "__main__":
    main()

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
