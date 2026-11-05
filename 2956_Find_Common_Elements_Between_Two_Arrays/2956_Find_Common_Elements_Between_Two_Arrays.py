class Solution:
    def findIntersectionValues(self, nums1, nums2):
        res = []
        cnt = 0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                cnt += 1
        
        res.append(cnt)

        cnt = 0
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                cnt += 1
        
        res.append(cnt)

        return res