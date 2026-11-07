class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = {}

        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
        
        s = set()
        for v in d.values():
            if v not in s:
                s.add(v)
            else:
                return False
        
        return True