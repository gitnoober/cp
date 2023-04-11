from collections import Counter, defaultdict


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        d = defaultdict(list)
        n1 = len(s1)
        n2 = len(s2)
        if n1 != n2:
            return False
        if Counter(s1) != Counter(s2):
            return False

        def recur(s):
            n = len(s)
            if n == 1 :
                return s
                
            for i in range(n):
                x = s[:i]
                y = s[i:]
                if x and y :
                    
                else:
                    return False
                

        # for i in range(n1):
            # print(s1[:i], s1[i:])

        """
        a b c d e
        abc   de

        ab c d e

        cba  ed
        decba

        """


s1 = "abcdbdacbdac"
s2 = "bdacabcdbdac"
obj = Solution().isScramble(s1, s2)
print(obj)
