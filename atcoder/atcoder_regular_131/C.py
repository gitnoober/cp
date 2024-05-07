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


n = int(input())
a = list(map(int, input().split()))
# bits = {i: [] for i in range(32)}

# for i in a:
#     for k in range(32):
#         if (1 << k) & i:
#             bits[k].append(i)

# for i in range(32):
#     if bits[i]:
#         debug("i, bits", i, bits[i])
bits = [0] * 32

for i in a:
    for k in range(32):
        if (1 << k) & i:
            bits[k] += 1

ok = False
for i in a:
    x = bits[:]
    for j in range(32):
        if (1 << j) & i:
            x[j] -= 1
    fl = 0
    for j in range(32):
        if x[j] % 2:
            fl = 1
    if fl == 0:
        ok = True

if ok:
    print("Win")  # if removing one element is a winning state then its trivial
else:
    print("Win" if n % 2 else "Lose")
    # there will always be atleast one bit that occurs an odd number of  times , so ultimately it will boil down to removing elements till the last one
