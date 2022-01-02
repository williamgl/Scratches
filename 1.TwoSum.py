class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            rest = target - nums[i]
            if rest in nums:
                j = nums.index(rest)
                if i!= j:
                    return [i, j]
