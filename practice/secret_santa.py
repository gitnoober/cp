inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)


def solve():
    for __ in range(*maps()):
        n, = maps()
        a = list(maps())
        acopy = a.copy()
        vis, pos, used = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            if not used[a[i]]:
                used[a[i]] = vis[i] = 1
                pos[a[i]] = i

        s = collections.deque()
        for i in range(1, n + 1):
            if not used[i]:
                s.append(i)

        for i in range(n):
            if not vis[i]:
                nxt = s[0]
                if nxt != i + 1:
                    a[i] = nxt
                    pos[a[i]] = i
                    used[a[i]] = 1
                else:
                    idx = pos[a[i]]
                    a[i] = nxt
                    a[i], a[idx] = a[idx], a[i]
                    pos[a[i]], pos[a[idx]] = i, idx

                s.popleft()

        tot = sum(a[i] == acopy[i] for i in range(n))
        print(tot)
        print(*a)


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
