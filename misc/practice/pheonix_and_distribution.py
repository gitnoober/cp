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


for _ in range(*maps()):
    n, k = maps()
    s = sorted(input().rstrip("\n"))
    if s[0] == s[k - 1]:
        if s[min(k, n - 1)] != s[n - 1]:
            print("".join(s[k - 1 :]))
        else:
            ans = s[k - 1]
            avg = (n - k + k - 1) // k
            for i in range(n - 1, -1, -1):
                if avg:
                    ans += s[i]
                    avg -= 1
            print(ans)
    else:
        ans = s[k - 1]
        print(ans)

    # distribute s into k non-empty strings and minimize the maximum lexicographic string
