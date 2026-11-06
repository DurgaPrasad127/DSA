class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        #97-122
        for l in letters:
            if ord(l) > ord(target):
                return l
        
        return letters[0]