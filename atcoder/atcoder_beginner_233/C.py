
import bisect as bs
import heapq as hp
import itertools as it
import math as mt
import operator as op
import os
import sys

from collections import ChainMap
from collections import Counter
from collections import OrderedDict
from collections import _chain
from collections import defaultdict
from collections import deque
from functools import reduce
from io import BytesIO
from io import BytesIO
from io import IOBase
from io import IOBase
def nCr(n, r): return reduce(op.mul, range(n - r + 1, n + 1), 1) // mt.factorial(r)

def ceil(a, b): return (a + b - 1) // b

def lcm(a, b): return a * b // mt.gcd(a, b)


gcdm = lambda *args: reduce(mt.gcd, args, 0)

def lcm(a, b): return a * b // mt.gcd(a, b)


lcmm = lambda *args: reduce(lcm, args, 1)

_str = str
str = lambda x=b"": x if type(x) is bytes else _str(x).encode()

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")

# end region

############################### THINK ABOUT THE EDGE CASES ###############################


# mod = int(1e9) + 7
inf = float('inf')

def linp(): return map(int, input().split())


def solve():
    n, x = map(int, input().split())


solve()
