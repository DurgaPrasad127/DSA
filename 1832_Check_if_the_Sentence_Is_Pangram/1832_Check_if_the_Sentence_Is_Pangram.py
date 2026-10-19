class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for i in sentence:
            if i not in s:
                s.add(i)
                
        return len(s) == 26 