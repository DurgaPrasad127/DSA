class Solution:
    def finalString(self, s: str) -> str:
        res = ''
        for ch in range(len(s)):
            if s[ch] != 'i':
                res += s[ch]
            else:
                res = res[::-1]
        
        return res