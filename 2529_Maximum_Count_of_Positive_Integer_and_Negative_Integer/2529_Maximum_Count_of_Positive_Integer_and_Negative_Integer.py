class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        minus = 0
        plus = 0

        for num in nums:
            if num < 0:
                minus += 1
            if num > 0:
                plus += 1
        
        return max(minus,plus)