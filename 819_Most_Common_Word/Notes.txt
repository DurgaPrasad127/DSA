class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = ''.join(ch.lower() if ch.isalpha() else ' ' for ch in paragraph)
        lw = words.split()
        bs = set(banned)
        d = {}
        for i in range(len(lw)):
            if lw[i] not in bs:
                if lw[i] in d:
                    d[lw[i]] += 1
                else:
                    d[lw[i]] = 1
        do = sorted(d, key=d.get, reverse=True)
        return do[0]