import os
import sys
import time
import math
import pprint
import itertools as it
import operator as op
import bisect as bs
import functools as fn
from collections import deque, defaultdict, OrderedDict, Counter, ChainMap
maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)
def nCr(n, r): return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)


def ceil(n, x): return (n + x - 1) // x


osi, oso = '/home/priyanshu/Documents/cp/input.txt', '/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
    sys.stdin = open(osi, 'r')
    sys.stdout = open(oso, 'w')

input = sys.stdin.readline

def maps(): return map(int, input().split())

# THINK ABOUT THE EDGE CASES ..........


def func(grid):
    n = len(grid[0])
    q ,level = deque([(i, j) for i in range(n) for j in range(n) if grid[i][j]]) , -1
    if len(q) == n*n or not len(q) :return -1
    t = [(-1 , 0) , (1, 0) , (0 , -1) , (0 , 1)]
    while q :
        for _ in range(len(q)):
            r , c = q.popleft()
            for I,J in t:
                i , j = r+I , c +J
                if i >=0 and i < n and j>=0 and j < n and not grid[i][j]:
                    grid[i][j] = 1 #it's already visited so mark it
                    q.append((i,j))
        level+=1 # the more time's it executes the deeper level it goes , because at first iteration it goes left , right , up and down and the next iteration(after len(q) iterations are processed) it goes in another left , right , up and down thus making the distance increase by 1.
    return level

grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(func(grid))
