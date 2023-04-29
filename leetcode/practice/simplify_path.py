class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split("/")
        st = []
        for i in p:
            if st and i == "..":
                st.pop()
            elif i != "" and i != "." and i != "..":
                st.append(i)

        if not st:
            return "/"
        res = []
        while st:
            res.insert(0, st.pop())
            res.insert(0, "/")
        return "".join(res)


# path = "/../"
# path = "/home/"
# path = "/home//foo/"
path = "/a/./b/../../c/"
obj = Solution().simplifyPath(path)
print(obj)
