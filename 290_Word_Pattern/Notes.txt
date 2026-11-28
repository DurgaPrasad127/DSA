class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        sl = s.split()
        if len(p) != len(sl):
            return False

        pairs = set()
        for i in range(len(p)):
            pairs.add((p[i],sl[i]))
        
        return len(pairs) == len(set(p)) == len(set(sl))