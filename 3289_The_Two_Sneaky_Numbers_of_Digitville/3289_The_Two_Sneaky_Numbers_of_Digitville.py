class Solution:
    def getSneakyNumbers(self, nums):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        res = []
        for k,v in d.items():
            if v == 2:
                res.append(k)
        return res