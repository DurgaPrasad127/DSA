class Solution:
    def checkString(self, s: str) -> bool:   
        i = 1
        while i < len(s):
            #print(s[i-1:i+1])
            if s[i-1:i+1] == 'ba':
                return False
            i += 1
        return True

class Solution:
    def checkString(self, s: str) -> bool:   
        return 'ba' not in s