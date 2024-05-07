def word_break(s, words):
    n = len(s)
    d = [False] * n
    for i in range(n):
        for j in range(i + 1, n + 1):
            if s[i:j] in words and (i == 0 or (i > 0 and d[i - 1])):
                d[j - 1] = True
    return d[-1]


s = "catsandog"
words = ["cats", "dog", "sand", "and", "cat"]
res = word_break(s, words)
print(res)

"""
Time Complexity -- O(n*n*n)
"""
