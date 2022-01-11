class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        nums.sort()

        if len(nums) < 3:
            return ans

        for i in range(len(nums) - 2):
            if nums[i] > 0: return ans

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
        return ans
