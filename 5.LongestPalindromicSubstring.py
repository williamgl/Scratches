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
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(string, left, right):
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1
            return string[left+ 1: right]
        ans = ''
        for i in range(len(s)):
            # odd numbers
            ans1 = getPalindrome(s, i, i)
            # even numbers
            ans2 = getPalindrome(s, i, i + 1)
            ans = max([ans, ans1, ans2], key=lambda x: len(x))
        return ans