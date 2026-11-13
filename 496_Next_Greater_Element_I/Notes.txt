class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        
        for num in nums1:
            idx = nums2.index(num)
            ans = -1

            for j in range(idx+1,len(nums2)):
                if nums2[j] > num:
                    ans = nums2[j]
                    break
            
            res.append(ans)
        
        return res