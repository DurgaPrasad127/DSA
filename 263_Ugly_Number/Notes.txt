class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = []
        i = 2

        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                n //= i
            else:
                i += 1

        if n > 1:
            factors.append(n)

        for f in factors:
            if f == 2 or f == 3 or f == 5:
                pass
            else:
                return False

        return True