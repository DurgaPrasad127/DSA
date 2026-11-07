class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = {"a","e","i","o","u"}
        vc = 0
        for i in range(k):
            if s[i] in v:
                vc += 1
        mvc = vc
        print(vc)
        for i in range(k,len(s)):
            if mvc == k:
                return k
            
            if s[i] in v:
                vc += 1
            
            if s[i-k] in v:
                vc -= 1
            
            mvc = max(vc,mvc)
        
        return mvc