class Solution:
    def judgeCircle(self, moves: str) -> bool:
        i = j = 0
        for k in range(len(moves)):
            if moves[k] == "L":
                i -= 1
            elif moves[k] == "R":
                i += 1
            elif moves[k] == "U":
                j += 1
            else:
                j -= 1        
        return i == 0 and j == 0