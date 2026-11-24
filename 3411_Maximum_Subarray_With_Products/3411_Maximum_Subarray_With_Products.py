import math
class Solution:
    def maxLength(self, nums) -> int:
        res = 0
        for i in range(len(nums)):
            pv = nums[i]
            gv = nums[i]
            lv = nums[i]
            for j in range(i+1,len(nums)) :
                pv = pv * nums[j]
                gv = math.gcd(gv,nums[j])
                lv = math.lcm(lv,nums[j])
                if pv > gv * lv:
                    break
                if pv == gv * lv:
                    res = max(res,j-i+1)
        return res