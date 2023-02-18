class Solution:
    def addToArrayForm(self, num, k: int):
        k = str(k)
        n = len(num)
        j = len(k) - 1
        carry = 0
        for i in range(n - 1, -1, -1):
            if j >= 0:
                x = int(num[i]) + carry + int(k[j])
                x = str(x)
                if len(x) > 1:
                    num[i] = int(x[-1])
                    pn = len(x)
                    carry = int(x[: pn - 1])
                else:
                    carry = 0
                    num[i] = int(x)
                j -= 1
            else:
                x = carry + int(num[i])
                x = str(x)
                if len(x) > 1:
                    num[i] = int(x[-1])
                    pn = len(x)
                    carry = int(x[: pn - 1])
                else:
                    carry = 0
                    num[i] = int(x)
        while j >= 0:
            x = carry + int(k[j])
            x = str(x)
            if len(x) > 1:
                num.insert(0, int(x[-1]))
                pn = len(x)
                carry = int(x[: pn - 1])
            else:
                carry = 0
                num.insert(0, int(x))
            j -= 1
        if carry:
            carry = str(carry)
            for i in carry[::-1]:
                num.insert(0, int(i))
        return num


# num, k = [1, 2, 0, 0], 34
# num, k = [2, 7, 4], 181
# num, k = [2, 1, 5], 806
# num = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
# k = 1
num = [0]
k = 23
obj = Solution().addToArrayForm(num, k)
print(obj)
