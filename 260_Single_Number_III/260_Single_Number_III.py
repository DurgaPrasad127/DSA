class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        res = []
        for k,v in d.items():
            if v == 1:
                res.append(k)
    
        return res