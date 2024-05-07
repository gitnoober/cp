# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
# mod = int(1e9) + 7
# mod = 998244353


def solve():

    def ask(i, j):
        print("?", i + 1, j + 1, flush=True)
        (x,) = linp()  # pi % pj
        return x

    (n,) = linp()
    res = [-1] * n

    i, j = 0, n - 1
    cnt = 0
    while i < n and j > -1:
        if (res[i] != -1 and res[j] != -1) or (i == j):
            i += 1
            j -= 1

        else:
            q1 = ask(i, j)
            q2 = ask(j, i)

            if q1 > q2:
                res[i] = q1
                i += 1
            else:
                res[j] = q2
                j -= 1
            cnt += 1

        if cnt == n - 1:
            break

    check = [False] * (n + 1)
    idx = -1

    for i in range(n):
        if res[i] == -1:
            idx = i
            continue

        check[res[i]] = True

    for i in range(1, n + 1):
        if not check[i]:
            res[idx] = i
            break

    print("!", *res, flush=True)


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
