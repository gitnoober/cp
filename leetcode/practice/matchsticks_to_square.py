class Solution:
    def makesquare(self, matchsticks) -> bool:
        n = len(matchsticks)
        s = sum(matchsticks)
        arr = [0] * 4

        def dfs(idx, arr, target):
            if idx == n:
                return arr[0] == arr[1] == arr[2] == arr[3]
            for i in range(4):
                if arr[i] + matchsticks[idx] > target:
                    continue
                j = i - 1
                while j >= 0:
                    if arr[i] == arr[j]:
                        break
                    j -= 1
                if j != -1:
                    continue

                arr[i] += matchsticks[idx]
                if dfs(idx + 1, arr, target):
                    return True
                arr[i] -= matchsticks[idx]
            return False

        if s % 4:
            return False
        target = s // 4
        for val in matchsticks:
            if val > target:
                return False

        return dfs(0, arr, target)


matchsticks = [1, 1, 2, 2, 2]
obj = Solution().makesquare(matchsticks)
print(obj)
