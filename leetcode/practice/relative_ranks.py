from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # def func():
        a = sorted([(i, j) for i, j in enumerate(score)])
        p = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        idx = 0
        for i, j in a:
            if idx <= 2:
                score[i] = p[idx]
            else:
                score[i] = str(idx + 1)
            idx += 1
        return score
