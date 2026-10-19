class Solution:
    def numberGame(self, nums):
        nums.sort()
        i = 0
        while(i < len(nums)-1):
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i=i+2
        return nums