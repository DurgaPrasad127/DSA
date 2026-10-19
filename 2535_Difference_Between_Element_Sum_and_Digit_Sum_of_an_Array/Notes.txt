class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        esum = 0
        for i in nums:
            esum += i
        
        dsum = 0
        for i in nums:
            while i > 9:
                dsum += i % 10
                i //= 10
            dsum += i
        
        return abs(esum - dsum)