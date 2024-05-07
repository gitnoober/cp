# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import io
import os
from math import gcd

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")


def lcm(a, b):
    return (a * b) // gcd(a, b)


def f(a, b):
    return abs(gcd(a, b) - lcm(a, b))


def is_prime(n):
    """returns True if n is prime else False"""
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True


def solve():

    (n,) = linp()
    if is_prime(n):
        return n + 1

    if n % 2 == 0:
        return n + (n // 2)

    mx = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            mx = max(mx, i)
            mx = max(mx, n // i)

    return n + mx

    # if n is prime -- > f(n , n + 1)
    # if n is even -- > f(n , n + (n//2))
    # if n is odd  -- > f(n , n + biggest number which divides n)


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
        print(solve())
