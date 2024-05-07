from math import gcd


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


def lcm(a, b):
    return (a * b) // gcd(a, b)


l = list(map(int, input().split()))
k = min(l)
l.remove(k)

lc = 1
totrem = 0
for i in l:
    lc = lcm(lc, i)
    totrem += i % k
    # print(totrem, k % i, i)
xp = None
if is_prime(lc + k + totrem):
    lc += k + totrem
    xp = lc
    ok = True
    for i in l:
        if lc % i != k:
            ok = False
    if ok:
        if lc > 10**10:
            print("None")
        else:
            print(lc)
    else:
        print("None")
else:
    print("None")
