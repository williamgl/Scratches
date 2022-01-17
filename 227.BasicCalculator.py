class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = '+'
        stack = []

        for i in s + '+':
            if i.isdigit():
                num = num * 10 + int(i)
            elif i in '+-*/':
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    temp = stack[-1] * num
                    stack[-1] = temp
                if sign == '/':
                    temp = stack[-1] // num
                    if stack[-1] < 0 and stack[-1] % num != 0:
                        temp += 1
                    stack[-1] = temp
                sign = i
                num = 0
        return sum(stack)
