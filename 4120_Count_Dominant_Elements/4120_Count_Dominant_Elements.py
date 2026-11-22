class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        de = 0
        if len(nums) < 2:
            return 1
        if nums[0] >= nums[1]:
            de += 1
        if nums[-1] >= nums[-2]:
            de += 1
        for i in range(1,len(nums)-1):
            if nums[i] >= (nums[i-1] + nums[i+1]) / 2:
                de += 1
        return de