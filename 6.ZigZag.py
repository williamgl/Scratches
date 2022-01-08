class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        answer = ""

        zigzag = [''] * numRows
        reverse = False
        count = 0

        for i in s:
            zigzag[count] += i
            if reverse:
                count -= 1
            else:
                count += 1
            if count == numRows - 1 or count == 0:
                reverse = not reverse

        return answer.join(zigzag)