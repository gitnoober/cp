inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)


def solve():

    for _ in range(*maps()):
        n, = maps()
        s = [int(x) for x in input().strip()]

        if sorted(s) == s:
            print(0)
            continue

        # print(1)
        cnt0, cnt1 = 0, 0
        for i in s:
            if i == 1:
                cnt1 += 1
            else:
                cnt0 += 1
        need = 0
        for i in range(cnt0):
            if s[i] == 1:
                need += 1

        a = []
        for i in range(n):
            if s[i] == 1 and need > 0:
                need -= 1
                a.append(i + 1)

        for i in range(a[-1], n):
            if s[i] == 0:
                a.append(i + 1)

        print(1)
        print(len(a), *a)


if __name__ == '__main__':
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

    solve()
