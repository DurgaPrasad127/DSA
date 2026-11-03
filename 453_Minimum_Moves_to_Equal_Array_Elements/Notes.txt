class Solution:
    def minMoves(self, nums: list[int]) -> int:
        cnt = 0
        mnn = min(nums)

        for i in range(len(nums)):
            cnt += nums[i] - mnn 
        
        return cnt