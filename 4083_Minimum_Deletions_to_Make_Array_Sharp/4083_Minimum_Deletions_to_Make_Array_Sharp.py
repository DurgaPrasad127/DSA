class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        deletions = 0
    
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                deletions += 1
    
        return deletions
