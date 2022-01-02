class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        length = len(s)
        if s == s[::-1]:
            return True
        else: return False

# ever better:
 def isPalindrome(self, x: int) -> bool:
        s=str(x)
        return s==s[::-1]