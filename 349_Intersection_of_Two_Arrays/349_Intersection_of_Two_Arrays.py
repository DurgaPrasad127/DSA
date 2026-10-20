class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s = set()
        res = []
        if len(nums1) < len(nums2):
            nums = nums1
        else:
            nums = nums2
        
        for i in range(len(nums)):
            if nums[i] in nums1 and nums[i] in nums2:
                s.add(nums[i])
       
        while s:
            e = s.pop()
            res.append(e)     
        return res     