class Solution:
    def minimizeSum(self, nums) -> int:
        n = len(nums)
        nums.sort()

        if n <= 3:
            return 0
        
        return min(
            nums[n-1] - nums[2],
            nums[n-2] - nums[1],
            nums[n-3] - nums[0],
        )