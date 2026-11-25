class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        if s1 == s2:
            return []
            
        i = j = 0
        res = []
        while i < len(s1):
            t1 = ""
            t2 = ""
            if s1[i] == s2[i]:
                i += 1
                j += 1
            else:
                while i < len(s1) and s1[i] != s2[i]:
                    t1 += s1[i]
                    t2 += s2[i]
                    i += 1
                    j += 1
                res.append([t1,t2])
        return res