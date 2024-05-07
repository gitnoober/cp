import os
import sys
import collections

maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)
def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
def ceil(n, x):
    return (n + x - 1) // x
osi, oso = (
    "/home/priyanshu/Documents/cp/input.txt",
    "/home/priyanshu/Documents/cp/output.txt",
)
if os.path.exists(osi):
    sys.stdin = open(osi, "r")
    sys.stdout = open(oso, "w")

input = sys.stdin.readline


def maps():
    return map(int, input().split())


# THINK ABOUT THE EDGE CASES ..........
def solve1(a, n, k):
    A = [set() for _ in range(k)]
    d, freq, K = collections.defaultdict(list), collections.defaultdict(int), k
    for i in range(n):
        d[a[i]].append(i)
        freq[a[i]] += 1
    while K:
        K -= 1
        for i in freq:
            if freq[i] and i not in A[K]:
                A[K].add(i)
                freq[i] -= 1
    L = [len(i) for i in A]
    avg = sum(L) // k
    for i in range(k):
        ok, idx = True, i
        while ok and L[i] < avg and idx < k:
            if L[idx] <= avg:
                idx += 1
            else:
                x = A[i].symmetric_difference(A[idx])
                for j in x:
                    if j not in A[i]:
                        A[i].add(j)
                        A[idx].remove(j)
                        L[i] += 1
                        L[idx] -= 1
                        break
    print(min(len(i) for i in A))


def solve2(s):
    print(int(sum([min(s.count(i), 2) / 2 for i in set(s)])))


for _ in range(*maps()):
    s = input().rstrip("\n")
    n = len(s)
    # solve1([ord(i) for i in s], n, 2)
    solve2(s)
