import os
import sys

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
def f(arr, x):
    ans = 0
    for i in arr:
        ans |= i ^ x
    return ans


def check(arr):
    m = max(arr)
    ans = maxx
    for i in range(m + 10):
        T = f(arr, i)
        if T < ans:
            ans = T
            X = i
    return ans, X


for _ in range(*maps()):
    n = [*maps()][0]
    a = list(maps())
    if n == 1:
        print(a[0], 0)
        continue
    mx = max(a)
    le = len(bin(mx)[2:])
    x = ["0"] * le
    arr = [bin(i)[2:] for i in a]
    ok = [0] * le
    for i in range(n):
        el = arr[i]
        # print(el , len(el))
        idx = le - 1
        for j in range(len(el) - 1, -1, -1):
            if el[j] == "0":
                ok[idx] += 1
            idx -= 1
            # print(ok,el , j,el[j])
        # print(ok,"cur")
    # print(ok)
    for i in range(le):
        if not ok[i]:
            x[i] = "1"
    x = int("".join(x), 2)
    A = 0
    for i in a:
        t = i ^ x
        A |= t
    print(x, A)
    # print(ok,arr)
    # if A != check(a)[0]:
    # 	K = check(a)
    # 	print(a , A,x , K)
    # 	for i in a :
    # 		print(bin(i)[2:])
    # 	print(bin(K[0])[2:] , bin(K[1])[2:],ok,"ppp")
    # 	print()
