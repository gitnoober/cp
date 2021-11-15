inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps(): return [int(i) for i in input().split()]


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')


mod = 10**9 + 7
for _ in range(*maps()):
    n, = maps()
    a = list(maps())
    if min(a):
        print(pow(2, n - 1, mod))
        continue
    mx = [0] * (n + 1)
    m = 0
    for i in a:
        mx[i] += 1

    while m <= n and mx[m] > 0:
        m += 1

    req = [0] * m
    done = m
    dp = [-1] * n
    i = n - 1
    for j in range(n - 1, -1, -1):
        if a[j] < m:
            req[a[j]] += 1
            if req[a[j]] == 1:
                done -= 1
            while i != -1 and not done:
                dp[i] = j
                if a[i] < m:
                    req[a[i]] -= 1
                    done += req[a[i]] == 0
                i -= 1
    print(req, m)

    debug("dp", dp)

    # dp1 = [0] * n
    # pref = [1] + [0] * n
    # for i in range(n):
    #     if dp[i] != -1:
    #         dp1[i] = pref[dp[i]]

    #     pref[i + 1] = (pref[i] + dp1[i]) % n
    #     debug("dp1", dp1, pref)
    # print(dp1[-1])
