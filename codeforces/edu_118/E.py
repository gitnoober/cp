import os
import sys
from io import BytesIO, IOBase
import math as mt
import operator as op
from functools import reduce


def nCr(n, r):
    return reduce(op.mul, range(n - r + 1, n + 1), 1) // mt.factorial(r)


def ceil(a, b):
    return (a + b - 1) // b


def lcm(a, b):
    return a * b // mt.gcd(a, b)


def gcdm(*args):
    return reduce(mt.gcd, args, 0)


def lcm(a, b):
    return a * b // mt.gcd(a, b)


def lcmm(*args):
    return reduce(lcm, args, 1)

_str = str
def str(x=b""):
    return x if type(x) is bytes else _str(x).encode()

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


def input():
    return sys.stdin.readline().rstrip("\r\n")


# end region

############################### THINK ABOUT THE EDGE CASES ###############################


# mod = int(1e9) + 7
inf = float("inf")


def linp():
    return map(int, input().split())


def solve():
    n, m = map(int, input().split())
    arr = []
    labx, laby = -1, -1
    t = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    for i in range(n):
        inp = list(input().strip())
        arr.append(inp)

        for j in range(m):
            if inp[j] == "L":
                labx, laby = i, j

    q = [(labx, laby)]
    vis = [[False for j in range(m)] for i in range(n)]
    vis[labx][laby] = True

    while q:
        x, y = q.pop()
        cnt = 0
        for dx, dy in t:
            newx, newy = dx + x, dy + y
            if 0 <= newx < n and 0 <= newy < m and arr[newx][newy] == ".":
                cnt = 0

                for i, j in t:
                    rw, cl = newx + i, newy + j
                    if (
                        0 <= rw < n
                        and 0 <= cl < m
                        and not vis[rw][cl]
                        and arr[rw][cl] == "."
                    ):
                        cnt += 1

                if cnt <= 1:
                    vis[newx][newy] = True
                    arr[newx][newy] = "+"
                    q.append((newx, newy))

    for i in arr:
        print("".join(i))


"""
    So , 'L' is a winning state, so a cell is winning iff the number of free cells adjacent to it and the losing cells, is less than 2
    Game theory concept - In a directed graph, a cell is wining if
    1) one it's adjacent vertex leads to a losing state
    2) all of it's adjacent vertices leads to winning vertices , then that vertex itself is a losing vertex


"""


for i in range(int(input())):
    solve()
