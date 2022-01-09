# Time Limit Exceed
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        while nums[0] != nums[-1]:
            for i in range(len(nums) - 1):
                nums[i] += 1
            nums.sort()
            count += 1
        return count

