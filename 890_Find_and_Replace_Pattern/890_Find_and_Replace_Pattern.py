class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        d = {}
        n = 0
        p_arr = []
        res = []

        #Pattern:
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = n
                p_arr.append(n)
                n += 1
            else:
                p_arr.append(d[pattern[i]])
            
        
        for i in range(len(words)):
            d = {}
            n = 0
            t_arr = []
            for j in range(len(words[i])):            
                if words[i][j] not in d:
                    d[words[i][j]] = n
                    t_arr.append(n)
                    n += 1
                else:
                    t_arr.append(d[words[i][j]])

            if t_arr == p_arr:
                res.append(words[i])    

        return res