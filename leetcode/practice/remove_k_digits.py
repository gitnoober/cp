import collections


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        dic = collections.defaultdict(collections.deque)
        for i in range(len(num)):
            dic[int(num[i])].append(i)
        ans = ["" for _ in range(len(num))]

        for n in range(9, -1, -1):
            while dic[n] and k > 0:
                k -= 1
                dic[n].popleft()

        for i in dic:
            for j in dic[i]:
                ans[j] = str(i)
        # print(k)
        for num in range(1000000):
            if num * (num + 1) // 2 > 10**10:
                print(num, "pp")
                break
            # print(10**10 - (num * (num + 1) // 2))
        return ''.join(ans)


num = "1432219"
k = 2
obj = Solution().removeKdigits(num, k)
print(obj)
