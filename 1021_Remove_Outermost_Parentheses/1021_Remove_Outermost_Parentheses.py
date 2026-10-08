class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        balance = 0

        for i in s:
            if i == "(":
                if balance > 0:
                    res += i
                balance += 1
            
            else:
                balance -= 1
                if balance > 0:
                    res += i
        return res

#for Extra Pushing
