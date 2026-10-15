class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        rese = []
        reso = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                rese.append(nums[i])
            else:
                reso.append(nums[i])
        
        return rese + reso