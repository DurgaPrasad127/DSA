class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        pw = []
        for i in accounts:
            pw.append(sum(i))
        
        return max(pw)