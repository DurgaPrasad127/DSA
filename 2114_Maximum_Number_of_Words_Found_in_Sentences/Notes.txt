class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        mxw = 1
        for i in range(len(sentences)):
            spaces = 0
            for j in range(len(sentences[i])):
                if sentences[i][j] == " ":
                    spaces += 1
            words = spaces + 1
            mxw = max(words,mxw)
        return mxw
