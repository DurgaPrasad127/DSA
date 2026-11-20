class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n2 = len(candyType) // 2
        ct = len(set(candyType))

        return min(ct,n2)