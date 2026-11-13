class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        res = []
        for word in words:
            w = word.lower()

            if all(ch in r1 for ch in w):
                res.append(word)
            elif all(ch in r2 for ch in w):
                res.append(word)
            elif all(ch in r3 for ch in w):
                res.append(word)

        return res