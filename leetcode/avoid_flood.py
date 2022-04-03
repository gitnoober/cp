import heapq
import collections


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n = len(rains)
        lakes = collections.defaultdict(collections.deque)
        for i in range(n):
            lakes[rains[i]].append(i)

        seen = set()
        closest = []
        ans = []
        for i in range(n):
            if rains[i] in seen:
                return []
            if rains[i]:
                ans.append(-1)
                seen.add(rains[i])
                l = lakes[rains[i]]
                l.popleft()
                if l:
                    nxt = l[0]
                    heapq.heappush(closest, nxt)
            else:
                if not closest:
                    ans.append(1)
                else:
                    x = heapq.heappop(closest)
                    ans.append(rains[x])
                    seen.remove(rains[x])
        return ans


rains = list(map(int, input().split(",")))
# print(rains)
obj = Solution().avoidFlood(rains)
print(obj)
