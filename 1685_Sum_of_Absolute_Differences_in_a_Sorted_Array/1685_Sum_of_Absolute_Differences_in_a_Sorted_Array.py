class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        res = []

        for i in range(n):
            left = nums[i] * i - left_sum
            right = (total - left_sum - nums[i]) - nums[i] * (n - i - 1)

            res.append(left + right)
            left_sum += nums[i]

        return res
