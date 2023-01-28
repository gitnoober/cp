from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust) -> int:
        tree = defaultdict(set)
        for u, v in trust:
            tree[u].add(v)

        def check_judge(judge):
            for people in range(1, n + 1):
                if people == judge:
                    continue
                if judge not in tree[people]:
                    return False
            return True

        ans = -1

        for node in range(1, n + 1):
            # print(node, tree[node], check_judge(node))
            if len(tree[node]) == 0 and check_judge(node):
                ans = node
                break
        return ans


n = 2
trust = [[1, 2]]
obj = Solution().findJudge(n, trust)
print(obj)
