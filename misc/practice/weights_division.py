inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger

# sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f"{msg}={pprint.pformat(args)}")


def solve():
    n, s = maps()
    gr = [[] for _ in range(n)]
    for i in range(n - 1):
        x, y, w = maps()
        x -= 1
        y -= 1
        gr[x].append([y, w])
        gr[y].append([x, w])

    cnt = [0] * n
    st = [0]
    vis = [False] * n
    p = [0] * n
    while st:
        node = st[-1]

        if not vis[node]:
            vis[node] = True

            for child, wt in gr[node]:
                if not vis[child]:
                    st.append(child)
                    p[child] = node

        else:
            if len(gr[node]) == 1:
                cnt[node] = 1
            else:
                for child, wt in gr[node]:
                    cnt[node] += cnt[child]

            st.pop()

    tot = 0
    h = []

    for u in range(n):
        for v, w in gr[u]:
            if v == p[u]:
                tot += w * cnt[u]

                W = w
                while W > 0:
                    h.append((W - (W // 2)) * cnt[u])
                    W //= 2

    h.sort(reverse=True)
    idx = 0
    while tot > s:
        tot -= h[idx]
        idx += 1

    print(idx)


if __name__ == "__main__":
    (tc,) = maps()
    while tc > 0:
        tc -= 1
        solve()
