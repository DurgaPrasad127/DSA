class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        mx_cnt = 0
        cnt = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
                
            mx_cnt = max(mx_cnt,cnt)
            
        return mx_cnt