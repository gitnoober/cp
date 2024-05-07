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


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) != n or n == 1:
        return "YES"

    tree = [0] * (n + 10)

    def get_sum(i):
        s = 0
        while i > 0:
            s += tree[i]
            i -= i & -i
        return s

    def get_sum_segment(s, t):
        ans = get_sum(t) - get_sum(s - 1)
        return ans

    def add(i, x):  # index , value
        while i <= n:
            tree[
                i
            ] += x  # updating all the positions in the tree which are responsible for this index
            i += i & (-i)

    invcnt = 0
    for i in range(n - 1, -1, -1):
        invcnt += get_sum(a[i] - 1)
        print(get_sum(a[i] - 1), a[i])
        add(a[i], 1)

    return "NO" if invcnt % 2 else "YES"


for i in range(int(input())):
    print(solve())

"""
	the parity of a permutation is (-1) ^ (total number of inversions)
	transposition - a set of length 2 which is a cycle
	if the parity of the permutation is even that means that the permuation has even number of transpositions (a cycle of length 3 has 2 transposition i->j, j->k)
	** a permutation with duplicates has even parity

"""
