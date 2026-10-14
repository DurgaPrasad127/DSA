class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        #if original not in nums:
            #return original
        
        for _ in range(len(nums)):
            if original in nums:
                original *= 2
        
        return original
        