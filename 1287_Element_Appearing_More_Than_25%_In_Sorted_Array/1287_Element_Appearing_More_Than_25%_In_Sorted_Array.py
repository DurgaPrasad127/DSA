class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        tfp = len(arr) // 4

        for i in range(len(arr) - tfp):
            if arr[i] == arr[i + tfp]:
                return arr[i]