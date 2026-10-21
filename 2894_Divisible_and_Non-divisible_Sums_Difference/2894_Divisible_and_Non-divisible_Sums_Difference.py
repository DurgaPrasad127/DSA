class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        dm = []
        ndm = []
        for i in range(1,n+1):
            if i % m == 0:
                dm.append(i)
            else:
                ndm.append(i)
        
        return sum(ndm)-sum(dm) 