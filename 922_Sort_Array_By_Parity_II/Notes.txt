class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        rese = []
        reso = []
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                rese.append(nums[i])
            else:
                reso.append(nums[i])
        
        res = []
        for i in range(len(max(rese,reso))):
            res.append(rese[i])
            res.append(reso[i])
        
        return res