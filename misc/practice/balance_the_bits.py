inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)


def solve():

    (tc,) = maps()

    for i in range(tc):
        (n,) = maps()
        s = input()
        a, b = [], []

        if s[0] == s[-1] == "1":
            k = s.count("1")
            if k % 2:
                print("NO")
            else:
                c = alt = 0
                for i in range(n):
                    if s[i] == "1":
                        if c < k // 2:
                            a += ["("]
                            b += ["("]
                        else:
                            a += [")"]
                            b += [")"]
                        c += 1
                    else:
                        if alt == 0:
                            a += ["("]
                            b += [")"]
                        else:
                            a += [")"]
                            b += ["("]
                        alt ^= 1
                a = "".join(a)
                b = "".join(b)
                print("YES", a, b, sep="\n")

        else:
            print("NO")


if __name__ == "__main__":
    # input = sys.stdin.buffer.readline
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
