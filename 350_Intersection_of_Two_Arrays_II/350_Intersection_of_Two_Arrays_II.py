class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []

        if len(nums1) < len(nums2):
            nums = nums1
            other = nums2
        else:
            nums = nums2
            other = nums1

        for i in range(len(nums)):
            if nums[i] in other:
                res.append(nums[i])
                other.remove(nums[i])

        return res