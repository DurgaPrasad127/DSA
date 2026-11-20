class Solution:
    def minOperations(self, nums, k: int) -> int:
        ops = 0
        arr = []
        for i in range(1,k+1):
            arr.append(i)
            
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in arr:
                arr.remove(nums[i])
            ops += 1

            if not arr:
                return ops