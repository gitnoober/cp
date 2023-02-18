class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        na = len(a)
        nb = len(b)
        if na < nb:
            a = ("0" * (nb - na)) + a
        else:
            b = ("0" * (na - nb)) + b
        carry = 0
        mx = max(na, nb)
        # print(a, b, "pp")
        for x in range(mx - 1, -1, -1):
            i, j = a[x], b[x]
            if i == j == "1":
                if carry:
                    ans.append("1")
                else:
                    ans.append("0")
                    carry ^= 1
            elif i == "1" or j == "1":
                if carry:
                    ans.append("0")
                else:
                    ans.append("1")
            else:
                if carry:
                    ans.append("1")
                    carry ^= 1
                else:
                    ans.append("0")
        if carry:
            ans.append("1")
        ans = "".join(ans[::-1])
        return ans


a = "1111"
b = "1111"
x = Solution().addBinary(a, b)
print(x)
"""
1  1 1 1
0  0 1 1
"""
