class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        bina = bin(a)[2:]
        binb = bin(b)[2:]

        onec = 0
        for i in bina:
            if i == '1':
                onec += 1

        s1 = onec

        onec = 0
        for i in binb:
            if i == '1':
                onec += 1

        s2 = onec

        if s1 >= s2:
            return s1*s2

        return s2//s1
        
        