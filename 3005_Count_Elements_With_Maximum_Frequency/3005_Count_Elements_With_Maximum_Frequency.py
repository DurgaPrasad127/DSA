class Solution:
    def maxFrequencyElements(self, nums) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        arr = list(d.values())
        arr.sort(reverse=True)
        
        mx = max(arr)
        res = 0
        for i in range(len(arr)):
            if arr[i] == mx:
                res += arr[i]
        
        return res