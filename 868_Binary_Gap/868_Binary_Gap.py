class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        mx = 0
        bg = 1
        for i in range(1,len(b)):
            if b[i] != '1':
                bg += 1
            else:
                mx = max(mx, bg)
                bg = 1
        return mx