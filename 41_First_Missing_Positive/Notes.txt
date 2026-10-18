class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
            
        for k in range(1, len(nums) + 1):
            if k not in d:
                return k  

        return len(nums)+1