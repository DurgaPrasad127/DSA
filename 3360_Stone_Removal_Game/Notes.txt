class Solution:
    def canAliceWin(self, n: int) -> bool:
        ab = 0
        x = 10
        
        while n >= x:
            n -= x
            x -= 1
            ab += 1
            
        return ab % 2 == 1