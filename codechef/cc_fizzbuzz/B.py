# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")


def solve():

    for _ in range(*linp()):
        (n,) = linp()
        s = input()
        ans = inf
        for c in "BW":
            j = 0
            cnt = 0
            while j < n:
                k = j + 1
                ok = False
                while j < n and s[j] == c:
                    j += 1
                    ok = True
                j = max(k, j)
                if ok:
                    cnt += 1
            ans = min(ans, cnt)
        print(ans)


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
