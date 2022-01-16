class Solution:
    def countAndSay(self, n: int) -> str:
        def say(n):
            string = str(n)
            ans = ''

            temp = string[0]
            count = 0

            for i in string:
                if temp == i:
                    count += 1
                else:
                    ans = ans + str(count) + temp
                    temp = i
                    count = 1
            ans = ans + str(count) + temp
            return ans
        ans = '1'
        while n > 1:
            ans = say(int(ans))
            n -= 1
        return ans