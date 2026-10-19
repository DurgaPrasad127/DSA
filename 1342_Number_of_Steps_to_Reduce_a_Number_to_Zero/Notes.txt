class Solution:
    def numberOfSteps(self, num: int) -> int:
        sp = 0
        while num >= 0:
            if num == 0:
                return sp
            elif num % 2 == 0:
                num /= 2
            else:
                num -= 1
            sp += 1
