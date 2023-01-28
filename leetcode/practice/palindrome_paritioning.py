class Solution:
    def check(self, string):
        st_arr = string.split(".")
        for i in st_arr:
            if i != i[::-1]:
                return False
        return True

    def partition(self, s: str):
        n = len(s)
        stack = [(s[0], 1)]  # string, next_index
        ans = []
        for string, next_index in stack:
            if next_index == n:
                if self.check(string):
                    ans.append(string.split("."))
            else:
                if string[-1] != ".":
                    y = (string + s[next_index], next_index + 1)
                    x = (string + ".", next_index)
                    stack.append(x)
                    stack.append(y)
                else:
                    y = (string + s[next_index], next_index + 1)
                    # stack.append(x)
                    stack.append(y)
            # break
        # print(ans)
        return ans


s = "aab"
obj = Solution()
ans = obj.partition(s)
print(ans)
