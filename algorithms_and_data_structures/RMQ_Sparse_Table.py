maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)


def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)


def ceil(n, x):
    return (n + x - 1) // x


def query(l, r, func):
    j = log[r - l + 1]
    return func(st[l][j], st[r - (1 << j) + 1][j])


def build(n, func=sum):
    log = [0] * n + [0]
    log[0] = 1
    for i in range(2, n + 1):
        log[i] = log[i // 2] + 1
    k = log[n]
    st = [[0 for _ in range(k + 1)] for __ in range(n)]
    for i in range(n):
        st[i][0] = a[i]

    for j in range(1, k + 1):
        i = 1
        while i + (1 << j) <= n:
            st[i][j] = func(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
            i += 1

    return st, log


# st[i][j] --> the value of func(sum/min/gcd) from ith position and of length 2**j till i + 2**j
# st[i][j] = func(st[i][2**(j-1)] , st[i + 2**(j-1)][j-1]) --- > i + 2**(j-1) to i + 2**(j-1) + 2**(j-1) = i + 2 **j
