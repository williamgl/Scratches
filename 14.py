class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            for j in range(len(strs)):
                if shortest[i] != strs[j][i]:
                    return shortest[:i]
        return shortest