class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        res = []
        for i in range(len(nums)):
            cnc = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    cnc +=1
            res.append(cnc)
        return res