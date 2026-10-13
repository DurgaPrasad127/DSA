class Solution:
    def rotatedDigits(self, n: int) -> int:
        gn = 0

        for i in range(1, n + 1):
            s = str(i)

            if any(digit in s for digit in "347"):
                continue

            if any(digit in s for digit in "2569"):
                gn += 1

        return gn