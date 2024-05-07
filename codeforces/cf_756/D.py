# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import io
import os

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")


def solve():

    (n,) = linp()
    b = list(map(lambda x: int(x) - 1, input().split()))
    p = list(map(lambda x: int(x) - 1, input().split()))

    root = -1
    for i in range(n):
        if b[i] == i:
            root = i
            break

    dist = [0] * n
    seen = {root}
    weights = [0] * n
    ok = True

    if p[0] == root:

        for i in range(1, n):
            if b[p[i]] not in seen:
                ok = False
                break

            d = i - dist[b[p[i]]]
            weights[p[i]] = d
            dist[p[i]] = dist[b[p[i]]] + d
            seen.add(p[i])

    else:
        ok = False

    print(*weights if ok else [-1])


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
        solve()
