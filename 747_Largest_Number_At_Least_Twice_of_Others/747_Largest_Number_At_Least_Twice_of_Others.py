class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        maxn = nums[0]
        ans = 0

        for i in range(1, len(nums)):
            if nums[i] > maxn:
                maxn = nums[i]
                ans = i

        for i in range(len(nums)):
            if i != ans and maxn < 2 * nums[i]:
                return -1

        return ans