class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        ns = set(nums)
        ls = list(ns)
        if len(ls) < 3:
            return max(nums)
        
        ns = set(nums)
        ls = list(ns)
        ls.sort()
        return ls[-3]

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        ns = set(nums)
        ls = list(ns)
        ls.sort()
        if len(ls) < 3:
            return ls[-1]
        return ls[-3]