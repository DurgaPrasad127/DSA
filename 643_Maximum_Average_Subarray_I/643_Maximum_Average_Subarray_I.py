class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        x = sum(nums[:k])
        mx = x

        for i in range(k,len(nums)):
            x += nums[i] - nums[i-k]
            mx = max(mx,x)
        
        return mx/k