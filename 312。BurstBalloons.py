class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = len(nums)
        nums = [1] + nums + [1]
        answer = 0

        def search(nums):
            answers = [0] * len(nums)

            if len(nums) > 5:
                i = nums[1:-1].index(max(nums[1:-1])) + 1
                if nums[i - 1] >= nums[i + 1]:
                    i -= 1
                else:
                    i += 1
            elif len(nums) == 5:
                i = 2
            elif len(nums) == 4:
                if nums[1] >= nums[2]:
                    i = 2
                else:
                    i = 1
            else:
                i = 1
            answers[i] = nums[i - 1] * nums[i] * nums[i + 1]
            return max(answers), answers.index(max(answers))

        while balloons >= 1:
            coins, index = search(nums)
            answer += coins
            nums.pop(index)
            balloons -= 1

        return answer
