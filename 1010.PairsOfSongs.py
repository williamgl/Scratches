# Time Limit Exceed
"""
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        length = len(time)

        for i in range(0, length - 1):
            for j in range(i+1, length):
                if (time[i] + time [j]) % 60 == 0:
                    count += 1
        return count
"""

# orders matter
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        zero = 0
        for i in range(len(time)):
            time[i] %= 60
            if time[i] == 0:
                zero += 1

        m = {}
        for i in time:
            if 60 - i in m:
                count += m[60 - i]
            if i in m:
                m[i] += 1
            else:
                m[i] = 1

        count += zero * (zero - 1) // 2