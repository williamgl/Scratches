class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, path, ans):
            if target < 0:
                return
            if target == 0:
                ans.append(path)
                return

            for i in range(len(nums)):
                dfs(nums[i:], target - nums[i], path + [nums[i]], ans)

        ans = []
        dfs(candidates, target, [], ans)
        return ans