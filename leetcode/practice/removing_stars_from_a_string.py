class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in s:
            if st and i == "*" and st[-1] != "*":
                st.pop()
                continue
            st.append(i)
        return "".join(st)


s = "leet**cod*e"
obj = Solution().removeStars(s)
print(obj)
