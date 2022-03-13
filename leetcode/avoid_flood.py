import collections


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n = len(rains)
        zeroes, lakes = collections.deque(), collections.deque()

        for i in range(n):
            if rains[i]:
                lakes.append(i)
            else:
                zeroes.append(i)
        ans = [-1] * n
        vis = set()

        for i in range(n):
            if rains[i] in vis:
                return []

            if rains[i]:
                vis.add(rains[i])
                lakes.popleft()
            else:
                ok = False
                zeroes.popleft()
                if len(zeroes):
                    nxt_zero = zeroes[0]
                    j = 0
                    while j < len(lakes) and lakes[j] < nxt_zero:
                        if rains[lakes[j]] in vis:
                            ans[i] = rains[lakes[j]]
                            vis.remove(rains[lakes[j]])
                            ok = True
                            break
                        j += 1

                if len(zeroes) == 0 or not ok:
                    j = 0
                    while j < len(lakes):
                        if rains[lakes[j]] in vis:
                            ans[i] = rains[lakes[j]]
                            vis.remove(rains[lakes[j]])
                            ok = True
                            break
                        j += 1

                    if not ok:
                        ans[i] = 1
                        vis.discard(1)

        return ans


rains = list(map(int, input().split(",")))
# print(rains)
obj = Solution().avoidFlood(rains)
print(obj)
