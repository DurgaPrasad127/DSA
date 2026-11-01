class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        mi = []

        i = 0
        while i < len(nums):
            mi.append(str(nums[i])+str(nums[i+1]))
            i += 2

        mi = list(map(int,mi))
        print(mi)
        return int(min(mi))