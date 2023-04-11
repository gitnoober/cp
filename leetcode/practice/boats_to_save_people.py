class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        n = len(people)
        i = 0
        j = n - 1
        ans = 0
        # print(people)
        while i <= j:
            # print(people[i], people[j], i, j)
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            ans += 1

        # print(i, j)
        # ans += j - i

        return ans


people = [3, 2, 2, 1]
limit = 3
obj = Solution().numRescueBoats(people, limit)
print(obj)
