class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(num):
            if (num % 2 == 0 and num != 2) or (num < 2):
                return False
            if num == 2:
                return True
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        if n >= 8 and n <= 11:
            return 11

        # all even length palindromes are divisible by 11
        for i in range(
            10 ** (len(str(n)) // 2), 10**5
        ):  # generating only the first half
            y = int(str(i) + str(i)[-2::-1])
            if y >= n and str(y) == str(y)[::-1] and isPrime(y):
                return y


obj = Solution().primePalindrome(1)
print(obj)
