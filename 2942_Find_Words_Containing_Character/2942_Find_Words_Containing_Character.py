class Solution:
    def findWordsContaining(self, words, x: str):
        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res