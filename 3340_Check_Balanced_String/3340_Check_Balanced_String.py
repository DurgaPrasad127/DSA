class Solution:
    def isBalanced(self, num: str) -> bool:
        n = len(num)
        even = 0
        odd = 0
        for i in range(n):
            if int(i) % 2 == 0:
                even += int(num[i])
            elif int(i) % 2 != 0:
                odd += int(num[i])
        
        if even == odd:
            return True
        
        return False