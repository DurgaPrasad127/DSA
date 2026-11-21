class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        if a > b + c:
            a = b + c
        elif b > a + c:
            b = a + c
        elif c > a + b:
            c = a + b

        return max(a,b,c) - min(a,b,c)