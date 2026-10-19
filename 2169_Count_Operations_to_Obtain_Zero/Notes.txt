class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        op = 0
        for _ in range(max(num1,num2)):
            if num1 == 0 or num2 == 0:
                break
            if num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            op += 1
        return op