class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        cnt = 0
        ans = 0
        for i in range(len(nums)):
            if minK <= nums[i] <= maxK:
                cnt += 1
            else:
                cnt = 0
            ans += cnt

        return ans
        