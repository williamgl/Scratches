# Time Limit Exceed
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        answer = 0

        if length == 1:
            return 1

        for i in range(0, length - 1):
            for j in range(i + 1, length + 1):
                if j - i > 90:
                    pass
                else:
                    string = s[i:j]
                    if self.check(string):
                        answer = max(answer, len(string))

        return answer

    def check(self, s):
        length = len(s)
        for i in range(0, length - 1):
            if s[i] in s[i + 1:]:
                return False
        return True
"""

# Best Solution
res = 0
word = ""
for c in s:
    if c not in word:
        word += c
        if len(word) > res:
            res = len(word)
    else:
        word = word[word.find(c) + 1:] + c
# return res
