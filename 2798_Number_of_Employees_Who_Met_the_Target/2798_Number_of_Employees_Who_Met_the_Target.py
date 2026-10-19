class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours, target: int) -> int:
        nemt = 0
        for h in hours:
            if h >= target:
                nemt += 1
        return nemt