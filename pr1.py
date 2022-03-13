class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""
        q, rem = divmod(abs(numerator), abs(denominator))
        res = [sign, str(q), "."]
        rems = {}
        while rem > 0 and rem not in rems:
            rems[rem] = len(res)
            q, rem = divmod(rem * 10, abs(denominator))
            res.append(str(q))

        if rem in rems:
            res.insert(rems[rem], "(")
            res.append(")")
        res = "".join(res).rstrip(".")
        return res


numerator = 4
denominator = 333
obj = Solution().fractionToDecimal(numerator, denominator)
print(obj)
