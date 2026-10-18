class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
            
        res = []
        for i in range(1,len(nums)+1):
            if i not in d:
                res.append(i)
        return res