class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = []
        
        for i in nums:
            if res.count(i) < k:
                res.append(i)
        
        return res
