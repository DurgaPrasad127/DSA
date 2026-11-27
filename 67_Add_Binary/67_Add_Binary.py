class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ad = int(a,2) + int(b,2)
        return bin(ad)[2:]