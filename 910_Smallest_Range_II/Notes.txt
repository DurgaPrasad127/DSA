class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        
        lemk = nums[-1] - k #Largest Element minus(-) k
        sepk = nums[0] + k #Smallest Element plus(+) k

        for i in range(1,len(nums)):
            high = max(nums[i-1] + k, lemk)
            low = min(sepk, nums[i] - k)
            ans = min(ans, high - low)
        
        return ans