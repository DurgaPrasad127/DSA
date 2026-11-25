class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        mn = float('inf')
        for i in range(len(nums) - k + 1):
            diff = nums[i+k-1] - nums[i]
            mn = min(mn,diff)
        return mn