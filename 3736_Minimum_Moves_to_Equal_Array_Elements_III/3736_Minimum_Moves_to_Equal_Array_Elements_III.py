class Solution:
    def minMoves(self, nums) -> int:
        cnt = 0
        mxn = max(nums)
        for i in range(len(nums)):
            if nums[i] != mxn:
                cnt += mxn - nums[i]
        
        return cnt