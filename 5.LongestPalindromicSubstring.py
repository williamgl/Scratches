""" Time Limit Exceed
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        for i in range(len(s)):
            for j in range(len(s) + 1, i + 1, -1):
                if s[i:j] == s[i:j][::-1] and j - i > len(answer):
                    answer= s[i:j]
        return answer

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=[s[i: j + 1] for i in range(len(s)) for j in range(i,len(s))]
        return max([i for i in l if i[::-1]==i],key=len)

"""