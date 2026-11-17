class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        sm = nums[0]
        mx = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                sm += nums[i]
            else:
                sm = nums[i]
            mx = max(mx,sm)

        return mx