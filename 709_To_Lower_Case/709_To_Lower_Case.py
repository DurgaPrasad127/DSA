class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for i in s:
            if ord(i) >= 65 and ord(i) <= 90:
                temp = ord(i) + 32
                res += chr(temp)
            else:
                res += i
        return res