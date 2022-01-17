class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, path, ans):
            if target < 0:
                return
            if target == 0:
                ans.append(path)
                return
            for i in range(len(nums)):
                if nums[i] not in nums[:i]:
                    dfs(nums[i + 1:], target - nums[i], path + [nums[i]], ans)
        ans = []
        candidates.sort()
        dfs(candidates, target, [], ans)
        return ans