class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        pd = 1
        sd = 0
        
        for i in range(len(s)):
            pd *= int(s[i])
            sd += int(s[i])
        
        return pd - sd