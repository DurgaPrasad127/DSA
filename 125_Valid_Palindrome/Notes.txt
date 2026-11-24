class Solution:
    def isPalindrome(self, s: str) -> bool:
        ftext = ''.join(ch.lower() for ch in s if ch.isalnum())
        return ftext == ftext[::-1]