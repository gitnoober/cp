# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")


def solve():  # calculate the maximum length substring with k '.' characters

    s = input()
    (k,) = linp()
    n = len(s)

    cnt = l = ans = 0

    for r in range(n):

        if s[r] == ".":
            cnt += 1

        while cnt > k:

            if s[l] == ".":
                cnt -= 1

            l += 1

        if r - l + 1 > ans:
            ans = r - l + 1

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
