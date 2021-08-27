import os
import sys
from io import BytesIO, IOBase
import math as mt
import itertools as it
import operator as op
import bisect as bs
import heapq as hp
from functools import reduce
from io import BytesIO, IOBase
from collections import deque, defaultdict, OrderedDict, Counter, ChainMap, _chain
maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)
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


def maps(): return map(int, input().split())

#   THINK ABOUT THE EDGE CASES ..........

#   DON'T SUBMIT UNLESS YOU ARE ABSOLUTELY SURE !!!!!


def naive(n,k):
	#O(n*n*k)
	dp = [[0 for _ in range(k+2)] for __ in range(n+1)]
	dp[0][1] = 1

	for i in range(1 , n):
		for K in range(1, k+2):
			for j in range(0 , i):
				if a[i] == a[j]:
					dp[i][K] = max(dp[i][K], dp[j][K] + 1)
				else:
					dp[i][K] = max(dp[i][K], dp[j][K-1] + 1)


#Too slow for Python even with fast I/O

for _ in range(*maps()):
	n,k = maps()
	a = [*maps()]
	
	last = [-1]*1001
	mx_ans = [0]*(k+1)
	dp = [[1 for _ in range(k+1)] for __ in range(n)]
	ans = 1
	for i in range(n):
		for j in range(k , -1 , -1):
			if j >= 1:
				dp[i][j] = mx_ans[j-1] + 1
				#dp[i][j] = pref[i-1][j] 

			if last[a[i]] != -1:
				dp[i][j] = max(dp[i][j], dp[last[a[i]]][j] + 1)

			# print(mx_ans, j , " before " , end =' ')

			mx_ans[j] = max(dp[i][j], mx_ans[j])

			# print(mx_ans)

			ans = max(ans , dp[i][j])

		last[a[i]] = i

	print(ans)


