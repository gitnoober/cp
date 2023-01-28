from collections import defaultdict


class Solution:
    def threeSum(self, nums):
        d = defaultdict(set)
        n = len(nums)
        ans = []
        for i in range(n):
            d[nums[i]].add(i)
        # print(d)
        se = set()
        if 0 in d and len(d[0]) > 2:
            ans.append([0, 0, 0])
            se.add((0, 0, 0))

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                diff = -(nums[i] + nums[j])
                if (nums[i], nums[j], diff) in se or diff not in d:
                    continue
                else:
                    # print("diff", diff, nums[i], nums[j])
                    if i in d[diff] or j in d[diff]:
                        if nums[i] == nums[j] == diff == 0:
                            continue
                        if len(d[diff]) > 1:
                            ans.append([nums[i], nums[j], diff])
                            op = [nums[i], nums[j], diff]
                            for a in range(3):
                                for b in range(3):
                                    if a == b:
                                        continue
                                    for c in range(3):
                                        if a == c or b == c:
                                            continue
                                        se.add((op[a], op[b], op[c]))

                    else:
                        ans.append([nums[i], nums[j], diff])
                        op = [nums[i], nums[j], diff]
                        for a in range(3):
                            for b in range(3):
                                if a == b:
                                    continue
                                for c in range(3):
                                    if a == c or b == c:
                                        continue
                                    se.add((op[a], op[b], op[c]))
        return ans


# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 0, 0]
# nums = [1, 2, -2, -1]
nums = [-1, 0, 1, 0]

obj = Solution().threeSum(nums)
print(obj)
