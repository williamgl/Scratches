# 亚麻
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = list()

        intervals.sort()

        for a, b in intervals:
            if answer and answer[-1][1] >= a:
                answer[-1][1] = max(answer[-1][1], b)
            else:
                answer.append([a, b])
        return answer
