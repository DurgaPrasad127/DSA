class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        res = [""] * len(rain)
        if rain[-1] == 1:
            res[-1] = "Bob"
        else:
            res[-1] = "None"
            
        a = b = 0
        for i in range(1,len(rain)):
            if rain[i-1] == rain[i] == 1:
                if a <= b:
                    res[i-1] += "Alice"
                    a += 1
                else:
                    res[i-1] += "Bob"
                    b += 1
            elif rain[i-1] == 1:
                res[i-1] += "Bob"
                b += 1
            else:
                res[i-1] += "None"
                
        return res