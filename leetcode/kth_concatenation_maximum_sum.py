class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        mod = 10**9 + 7
        pr, s = [], 0
        ok = True
        for i in arr:
            if i < 0:
                ok = False
            s += i
            pr.append(s)
        sf, s = [], 0
        for i in arr[::-1]:
            s += i
            sf.append(s)

        if ok:
            return (s * k) % mod
        else:
            ans = 0
            print(pr, "prefix")
            print(sf, "suffix")
            for i in range(len(arr)):
                ans = max(ans, pr[i])

        # some pre and then some suffix


arr = [1, -4, 3]
k = 3
obj = Solution().kConcatenationMaxSum(arr, k)
print(obj)
