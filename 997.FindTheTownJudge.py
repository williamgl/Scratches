class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        length = len(trust)
        townJudge = []

        def judge(i, n, trust):
            for j in range(1, n + 1):
                if i == j:
                    pass
                else:
                    if [j, i] not in trust:
                        return False
            for p in range(len(trust)):
                if i == trust[p][0]:
                    return False
            return True

        for i in range(1, n + 1):
            if judge(i, n, trust):
                townJudge += [i]

        if len(townJudge) == 1:
            return townJudge[0]
        else:
            return -1