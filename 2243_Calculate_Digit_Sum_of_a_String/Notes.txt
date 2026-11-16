class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ls = list(s)
            ta = []
            i = 0

            while i < len(s):
                group = ls[i:i+k]
                total = 0

                for digit in group:
                    total += int(digit)

                ta.append(str(total))
                i += k
            
            s = "".join(ta) 
        
        return s