class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        
        for i in range(n):
            if n % (i+1) == 0:
                arr.append(nums[i])

        sum_s = 0
        for i in range(len(arr)):
            sum_s += arr[i] * arr[i]

        return sum_s
        