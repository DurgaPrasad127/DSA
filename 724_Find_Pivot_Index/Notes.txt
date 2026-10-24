class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        lt = 0

        for i in range(len(nums)):
            rt = total - lt - nums[i]

            if lt == rt:
                return i
            
            lt += nums[i]
        
        return -1