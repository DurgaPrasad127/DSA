class Solution:
    def averageValue(self, nums: list[int]) -> int:
        arr = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] % 3 == 0:
                arr.append(nums[i])
        
        if len(arr) > 0:
            return sum(arr) // len(arr)
        return 0