inf = float("inf")
import sys
import pprint
import logging
from logging import getLogger
from math import gcd

sys.setrecursionlimit(10**7)


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


inn = [0] * 1000001
out = [0] * 1000001
flatentree = [0] * 1000001
parent = [0] * 1000001
gcd_subtree = [0] * 1000001
value = [0] * 1000001


def dfs(x, p):
    global timer
    parent[x] = p
    flatentree[timer] = x
    inn[x] = timer
    timer += 1
    gcd_subtree[x] = value[x]

    for child in v[x]:
        if child != p:
            gcd_subtree[x] = gcd(dfs(child, x), gcd_subtree[x])

    flatentree[timer] = x
    out[x] = timer
    timer += 1
    return gcd_subtree[x]


(t,) = maps()
while t:
    t -= 1
    timer = 1
    (n,) = maps()
    v = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = maps()
        v[a].append(b)
        v[b].append(a)

    value = [0] + [*maps()]
    dfs(1, -1)
    si = 2 * n
    forward = [0] * (si + 1)
    backward = [0] * (si + 1)
    forward[1] = backward[si] = value[1]

    for i in range(2, si + 1):
        forward[i] = gcd(forward[i - 1], value[flatentree[i]])

    i = si - 1
    while i >= 1:
        backward[i] = gcd(backward[i + 1], value[flatentree[i]])
        i -= 1

    ans = 1
    temp = 0
    for i in range(1, n + 1):
        children = []
        for child in v[i]:
            if child != parent[i]:
                children.append(gcd_subtree[child])

        if len(children) != 0:
            temp = 0
            for j in children:
                temp += j

            temp1 = 0
            if i != 1:
                temp1 = gcd(forward[inn[i] - 1], backward[out[i] + 1])
                ans = max(ans, temp + temp1)

            else:
                ans = max(ans, temp)

        else:
            temp = gcd(forward[inn[i] - 1], backward[out[i] + 1])
            ans = max(ans, temp)

    print(ans)
