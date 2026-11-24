class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in dic:
                dic[ss].append(s)
            else:
                dic[ss] = [s]
        return list(dic.values())