class Solution:
    @staticmethod
    def check_valid_ip(st):
        ok = True
        arr = st.split(".")
        if len(arr) != 4:
            return False
        for i in arr:
            if not i or int(i) > 255 or (len(str(int(i))) != len(i)):
                ok = False
        return ok

    def restoreIpAddresses(self, s: str):
        stack = [(s[0], 0, 1)]  # strint, number of dot's, last index
        n = len(s)
        ans = []
        for string, dot_cnt, index in stack:
            if index == n:
                res = self.check_valid_ip(string)
                if res:
                    ans.append(string)
                continue
            if dot_cnt == 3:
                x = (string + s[index], dot_cnt, index + 1)
                stack.append(x)
            else:
                x = (string + ".", dot_cnt + 1, index)
                y = (string + s[index], dot_cnt, index + 1)
                stack.append(x)
                stack.append(y)
        # print(ans)
        return ans


# s = "25525511135"
s = "0000"
obj = Solution().restoreIpAddresses(s)
print(obj)
