import sys
import pprint
import logging
from logging import getLogger
import bisect


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
maxn = 10**5


def ok(val):
    start = val
    ans = 0
    cnt = 0
    # print(start, r[m])
    while start <= r[m] and cnt < n:
        idx = max(0, bisect.bisect_right(r, abs(start)) - 1)
        v = 0
        sk = abs(start)
        if idx + 1 <= m:
            if r[idx] < sk <= r[idx + 1]:
                v = s[idx]
            elif r[idx] == sk:
                v = s[idx - 1]
        else:
            v = s[idx - 1]
        cnt += 1
        ans += v
        start += d
        # print(v, "pp", sk, idx, start - d)

    return ans


if __name__ == "__main__":
    n, m, d = map(int, input().split())
    r = list(map(int, input().split()))
    s = list(map(int, input().split()))
    l, h = -(10**1), 10**11
    ANS = -111

    while l <= h:
        mid = (l + h) >> 1
        if ok(mid) <= ANS:
            ANS = mid
            h = m - 1
        else:
            l = m + 1
        print(l, h, mid, ok(mid))

    print(ANS)
