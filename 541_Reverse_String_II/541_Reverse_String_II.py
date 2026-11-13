class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ls = list(s)
        i = 0

        while i < len(ls):
            ls[i:i+k] = ls[i:i+k][::-1]
            i += 2 * k

        return ''.join(ls)