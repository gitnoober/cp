from collections import defaultdict


class Solution:
    def distinctNames(self, ideas) -> int:
        all_first_alphabets = defaultdict(set)
        distinct = 0
        for i in ideas:
            all_first_alphabets[i[0]].add(i[1:])
        dic = sorted(all_first_alphabets.items())
        for pre1, suff1 in dic:
            for pre2, suff2 in dic:
                if pre2 >= pre1:
                    break
                common = len(suff1 & suff2)
                distinct += (len(suff1) - common) * (len(suff2) - common)
        return distinct * 2


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""


ideas = ["coffee", "donuts", "time", "toffee"]
ideas = ["aaa", "baa", "caa", "bbb", "cbb", "dbb"]
obj = Solution().distinctNames(ideas)
print(obj)
