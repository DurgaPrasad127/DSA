class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        Nangle = abs((30 * hour) - (5.5 * minutes))
        if Nangle > 180:
            return 360 - Nangle
        else:
            return Nangle