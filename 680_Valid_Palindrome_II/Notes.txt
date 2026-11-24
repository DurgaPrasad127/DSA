class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                skipl = s[i+1:j+1]
                skipr = s[i:j]
                return skipl == skipl[::-1] or skipr == skipr[::-1]
        return True