from itertools import permutations, combinations


def naive(n):
    v = ['a', 'e', 'i', 'o', 'u']
    t = []
    for i in v:
        t.extend([i] * n)
    cnt = 0
    se = set()

    for i in combinations(t, n):
        if sorted(i) == list(i):
            se.add(i)
    return len(se)


class ValidVowelString:
    def cntValidStrings(self, n):
        mod = 1000000007
        dp = [[0 for _ in range(5)] for __ in range(n + 1)]
        for i in range(5):
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(5):
                for k in range(5):
                    if k <= j:
                        """ k <= j , the number of strings which ends with j is equal to the number of strings with length i - 1 which ends with a smaller character than j + number of strings which end with j"""
                        dp[i][j] += dp[i - 1][k]
                        dp[i][j] %= mod

        res = 0
        for i in range(5):
            res += dp[n - 1][i]
            res %= mod
        return res
