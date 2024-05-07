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
from collections import defaultdict


def add(r1, r2):
    if len(r1) > len(r2):
        r2 = "0" * (len(r1) - len(r2)) + r2

    if len(r2) > len(r1):
        r1 = "0" * (len(r2) - len(r1)) + r1

    r1 = "0" + r1
    r2 = "0" + r2

    summ = 0
    carry = 0
    i = len(r1) - 1

    while i >= 0:
        x, carry = int(r1[i]) + int(r2[i]) + carry, 0

        if x >= 10:
            x, carry = x - 10, 1
        summ += x
        i -= 1
    return summ


def func(i, d1, d2, l1, l2):
    res1, res2 = [None] * (l1 + 1), [None] * (l2 + 1)

    for j in range(
        10 - i, 10
    ):  # the situation is optimal if the sum is good and if it is not then the goal is just to add a carry and more digits with sum 9 to the left
        if d1[i] and d2[j]:
            d1[i] -= 1
            d2[j] -= 1
            res1[l1] = i
            res2[l2] = j
            l1 -= 1
            l2 -= 1
            break

    for j in range(10):
        for k in range(9 - j, 10):
            # (3 , 6) -- > (3 , 7) --> (3 , 8) --> (3 , 9)
            while d1[j] and d2[k] and l1 >= 0 and l2 >= 0:
                d1[j] -= 1
                d2[k] -= 1
                res1[l1] = j
                res2[l2] = k
                l1 -= 1
                l2 -= 1

    for i in range(9, 0, -1):
        while d1[i]:
            res1[l1] = i
            l1 -= 1
            d1[i] -= 1

    for i in range(9, 0, -1):
        while d2[i]:
            res2[l2] = i
            l2 -= 1
            d2[i] -= 1

    return "".join(map(str, res1)), "".join(map(str, res2))


def main():
    a = list(map(int, input()))
    b = list(map(int, input()))
    d1, d2 = defaultdict(int), defaultdict(int)
    for i in a:
        d1[i] += 1

    for i in b:
        d2[i] += 1

    l1, l2 = len(a) - 1, len(b) - 1
    ans = float("inf")
    s1, s2 = None, None
    for i in range(1, 10):
        x, y = func(i, d1.copy(), d2.copy(), l1, l2)
        summ = add(x, y)

        if summ < ans:
            ans = summ
            s1, s2 = x, y

    print(s1, "\n", s2)


if __name__ == "__main__":
    main()
