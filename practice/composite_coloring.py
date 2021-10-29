import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]

from collections import defaultdict


def prime_sieve(n):
    """returns a sieve of primes >= 5 and < n"""
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    """returns a list of primes <= n"""
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend(3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1)
    return res


def type1():
    pr = prime_list((int(1000**0.5)+1))
    for _ in range(*maps()):
        n, = maps()
        a = [*maps()]

        occ = [0]*n
        for i in range(n):
            for j in range(11):
                if a[i]%pr[j]==0:
                    occ[i] = j + 1
                    break

        print(len(set(occ)))

        d = defaultdict(list)
        for i in range(n):
            d[occ[i]].append(i)
        idx = 1
        for i in d:
            for j in d[i]:
                occ[j] = idx
            idx+=1
        print(*occ)

    """
    composite number -- product of 2 positive numbers both greater than 1, that means it only has 2 divisors,
    which means d * k = n , where d is a prime <= n**0.5  and n is divisible by k , and coincidentally all the primes numbers that can be
    used by us is exactly 11, so group the numbers with the same smallest divisor.
    """
