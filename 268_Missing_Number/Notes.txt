class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        nums_sum = sum(nums)
        tot_sum = (N**2 + N)/2

        res = tot_sum - nums_sum
        return int(res)
        