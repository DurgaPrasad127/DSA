class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        ress = ""   
        i = 0
        for j in range(len(spaces)):
            curs = ""
            curs = s[i:spaces[j]] + " " 
            ress += curs
            i = spaces[j]
        
        ress += s[i:]
        return ress
