# n = 1 << 31
# print(bin(15)[2:])
# print(bin(9)[2:])
# print(bin(12)[2:])
# x = 3
# print(x << 1)
# print(6 << 1)

dividend = -2147483648
divisor = -1
def func(dividend, divisor):
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    ans = 0
    sign = 1 if (dividend > 0) == (divisor > 0 ) else - 1
    dividend = abs(dividend)
    divisor = abs(divisor)

    while dividend - divisor > 0 :
        temp = divisor
        m = 1
        while temp << 1 <= dividend:
            temp <<= 1
            m <<= 1
        ans += m
        dividend-=temp
        # print(dividend, divisor, m)
    return ans*sign

print(func(dividend, divisor))

