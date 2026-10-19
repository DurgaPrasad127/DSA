class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            tot = 0

            while num > 0:
                tot += num % 10
                num //= 10

            num = tot

        return num