class Solution:
    def minInsertions(self, s: str) -> int:
        openp = 0
        ins = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                openp += 1
                i += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ")":
                    if openp > 0:
                        openp -= 1
                    else:
                        ins += 1
                    i += 2
                else:
                    ins += 1
                    if openp > 0:
                        openp -= 1
                    else:
                        ins += 1
                    i += 1
        ins += 2 * openp
        return ins


            
                        
            

        