class Solution:
    def romanToInt(self, s: str) -> int:
        answer = [0] * len(s)

        def digit(num):
            if num == 'I':
                return 1
            elif num == 'V':
                return 5
            elif num == 'X':
                return 10
            elif num == 'L':
                return 50
            elif num == 'C':
                return 100
            elif num == 'D':
                return 500
            elif num == 'M':
                return 1000

        for i in range(len(s)):
            answer[i] = digit(s[i])

        for i in range(len(s) - 1):
            if answer[i] < answer[i + 1]:
                answer[i] *= -1
        return sum(answer)