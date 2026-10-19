class Solution:
    def countDigits(self, num: int) -> int:
        sn = str(num)
        ans = 0
        for i in sn:
            if num % int(i) == 0:
                ans += 1
        
        return ans
        