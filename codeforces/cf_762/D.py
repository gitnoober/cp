import sys
import pprint
import logging
from logging import getLogger


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


for _ in range(int(input())):
    input()
    m, n = map(int, input().split())  # number of shops , friends

    arr, A, mx, idx = [], [], [0] * n, [0] * n

    for i in range(m):
        a = list(map(int, input().split()))
        arr.append(a)
        A.append(sorted(enumerate(a), key=lambda x: -x[1]))

    for i in range(n):
        for j in range(m):
            if arr[j][i] > mx[i]:
                mx[i] = arr[j][i]
                idx[i] = j  # rows

    if len(set(idx)) != n:
        print(min(mx))
        continue

    # pick the maximum minimum pair

    p1 = p2 = f1 = f2 = mxx = 0

    for i in range(m):
        idx, val = A[i][1]
        if val > mxx:
            maxx, p1, p2, f1, f2 = val, A[i][0][1], A[i][1][1], A[i][0][0], A[i][1][0]

        if val == mxx:
            p1, f1, f2 = max(p1, A[i][0][1]), A[i][0][0], A[i][1][0]

    check = [False] * n
    check[f1] = check[f2] = True
    ans = min(p1, p2)

    for i in range(n):
        if check[i]:
            continue
        ans = min(ans, mx[i])

    print(ans)
