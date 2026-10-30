class Solution:
    def reverseByType(self, s: str) -> str:
        letters = []
        special = []

        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                special.append(ch)

        result = []

        for ch in s:
            if ch.isalpha():
                result.append(letters.pop())
            else:
                result.append(special.pop())

        return ''.join(result)