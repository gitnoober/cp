def is_prime(n):
    """returns True if n is prime else False"""
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True


def calc(a, b, f):
    x = a * b
    y = (b - a) ** 2
    xx = x / y
    return xx >= f


# def bi(a, f, mx):
#     l, h = 1, min(mx, 1000)
#     res = None
#     while l <= h:
#         diff = (l + h) >> 1
#         x = calc(a, a + diff, f)
#         if is_prime(a + diff):
#             if x:
#                 l = diff + 1
#             else:
#                 h = diff - 1
#             continue
#         if x:
#             res = a + diff
#             l = diff + 1
#         else:
#             h = diff - 1
#         print(a, a + diff, x, calc(a, a + diff, f))
#     return res


f, p1, p2 = map(int, input().split())


def check(l, h):
    res = None
    while l <= h:
        m = (l + h) >> 1

        # if is_prime(m + 1):
        #     if m + 2 <= h and calc(m, m + 2, f):
        #         res = m
        #         h = m - 1
        #     else:
        #         l = m + 1
        #     continue

        # if is_prime(m):
        #     if not is_prime(m + 1) and calc(m + 1, m + 2, f) and m + 2 <= h:
        #         res = m + 1
        #         h = m
        #     else:
        #         l = m + 1
        #     continue

        if calc(m, m + 1, f) >= f:
            res = m
            h = m - 1
        else:
            l = m + 1
    return res


x = check(p1, p2)
if x is None:
    print(None)
else:
    ok = False
    for y in range(x + 1, min(x + 1001, p2)):
        if calc(x, y, f) and not is_prime(y):
            ok = True
            print(x, y)
            break
    if not ok:
        print(None)


# for j in range(stop: int)


def op(a, b, f):
    x = a * b
    y = (b - a) ** 2
    xx = x / y
    print(xx, xx >= f)


"""
31 10 15
1729 1000 2000
123456 100 200
"""
