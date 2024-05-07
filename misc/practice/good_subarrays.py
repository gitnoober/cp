# DON'T SUBMIT UNLESS YOU'RE ABSOLUTELY SURE OR ATLEAST 70 % SURE !!!

import pprint
import logging
from logging import getLogger
import collections

# sys.setrecursionlimit(10 ** 9)

inf = float("inf")
# mod = int(1e9) + 7
# mod = 998244353


def search(arr, val, l):
    h = len(arr) - 1
    while l <= h:
        m = (l + h) >> 1
        if arr[m] - arr[l - 1] == val:
            return True
        elif arr[m] - arr[l - 1] < val:
            l = m + 1
        else:
            h = m - 1

    return False


def solve():

    (n,) = linp()
    a = [int(i) for i in input()] + [inf]
    p = [0]
    for i in a:
        p.append(p[-1] + i)

    prev = collections.defaultdict(int)
    ans = 0
    for i in range(n + 1):
        x = p[i] - i
        ans += prev[x]
        prev[x] += 1
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

    for _ in range(*linp()):
        solve()
