import sys
import pprint
import logging
from logging import getLogger


def input():
    return sys.stdin.readline().rstrip("\r\n")


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f"{msg}={pprint.pformat(args)}")


# 30 MINUTES ATLEAST !!!!

###################################################################################################################


def main():
    n, m, k = map(int, input().split())
    now = []
    need = []

    for i in range(k):
        now.append(list(map(int, input().split())))

    for i in range(k):
        need.append(list(map(int, input().split())))

    mx1, mx2 = 0, 0
    for i in range(k):
        if now[i][0] - mx1 > 1:
            mx1 = max(mx1, now[i][0]) - 1

        if now[i][1] - mx2 > 1:
            mx2 = max(mx2, now[i][1]) - 1

    need.sort()
    res = ["U"] * mx1 + ["L"] * mx2
    curR = curC = 1
    for i in range(k):
        dx = need[i][0] - curR
        dy = need[i][1] - curC

        if dx < 0:
            res += ["U"] * (-dx)
            curR += dx
        elif dx > 0:
            res += ["D"] * dx
            curR += dx

        if dy < 0:
            res += ["L"] * (-dy)
            curC += dy

        elif dy > 0:
            res += ["R"] * dy
            curC += dy

    print(len(res))
    print("".join(res))


if __name__ == "__main__":
    main()
