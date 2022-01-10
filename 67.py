class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def stringToInteger(n):
            answer = 0
            for i in range(len(n)):
                if n[len(n) - i - 1] == '1':
                    answer += 2**i
            return answer
        sumAB = stringToInteger(a) + stringToInteger(b)
        answer = []
        if sumAB == 0:
            return '0'
        while sumAB != 0:
            if sumAB % 2 == 0:
                answer.append('0')
            else: answer.append('1')
            sumAB = sumAB // 2
        ans = ''
        answer.reverse()
        for i in answer:
            ans += i
        return ans