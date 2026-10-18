class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
            
        res = []
        for k,v in d.items():
            if v > 1:
                res.append(k)
        for k in range(1, len(nums) + 1):
            if k not in d:
                res.append(k)    
        return res