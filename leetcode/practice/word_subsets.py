from collections import Counter


class Solution:
    def wordSubsets(self, words1, words2):
        c = Counter()
        for string in words2:
            c |= Counter(string)
        res = [string for string in words1 if not c - Counter(string)]
        return res


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
obj = Solution().wordSubsets(words1, words2)
print(obj)
