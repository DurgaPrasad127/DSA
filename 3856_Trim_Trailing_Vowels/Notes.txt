class Solution:
    def trimTrailingVowels(s:str):
        l = list(s)
        v = "aeiou"
        for i in range(len(l)-1,-1,-1):
            if l[i] in v:
                l.pop(i)
            else:
                break

        return "".join(l)
