class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        mx = 1
        cur = 1
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                cur += 1 
                mx = max(mx,cur)     
            else:
                cur = 1
            mx = max(mx,cur)

        return mx