class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        rs = ''
        for i in s:
            if i.isalpha():
              rs += i
        rs = rs[::-1]
        
        ls = list(s)
        i = 0
        j = 0
        while i < len(ls): 
            if ls[i].isalpha():
                ls[i] = rs[j]
                j += 1
            i += 1

        return ''.join(ls) 