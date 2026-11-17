class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if n == 0:
            return -1

        if n == 1:
            return 0

        for i in range(n):
            left = nums[:i+1]
            right = nums[i:n]

            if max(left) - min(right) <= k:
                return i

        return -1