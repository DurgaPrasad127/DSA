class Solution:
    def possibleStringCount(self, word: str) -> int:
        ps = 1
        for i in range(1,len(word)):
            if word[i-1] == word[i]:
                ps += 1
        
        return ps