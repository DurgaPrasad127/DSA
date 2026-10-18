class Solution:
    def shuffle(self, nums, n):
        nums2 = nums[n:]
        res = []

        for i in range(n):
            res.append(nums[i])
            res.append(nums2[i])

        return res