class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        res = []
        sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        for key in sorted_d.keys():
            res.append(key)
            if len(res) == k:
                break
        return res