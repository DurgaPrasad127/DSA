class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs = sorted(costs)
        mxb = 0
        i = 0
        while coins and i < len(costs):
            if costs[i] <= coins:
                coins -= costs[i]
                mxb += 1
            
            i += 1
        
        return mxb