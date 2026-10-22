class Solution:
    def canAliceWin(self, nums) -> bool:
        a = b = 0
        for i in range(len(nums)):
            if nums[i] <= 9:
                a += nums[i]
            else:
                b += nums[i]
        return a > b or b > a