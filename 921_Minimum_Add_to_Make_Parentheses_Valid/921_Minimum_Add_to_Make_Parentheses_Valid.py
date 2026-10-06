class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        additions = 0

        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    additions += 1

        return additions + len(stack)