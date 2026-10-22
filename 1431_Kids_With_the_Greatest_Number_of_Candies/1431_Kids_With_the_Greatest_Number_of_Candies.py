class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        mxc = max(candies)
        res = []
        for i in range(len(candies)):
            res.append(candies[i] + extraCandies >= mxc)
        return res