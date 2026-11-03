class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        ca = 0
        ma = 0
        for g in gain:
            ca += g
            if ca > ma:
                ma = ca
        
        return ma
        