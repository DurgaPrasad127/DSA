class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        result = sorted(nums, key=lambda x: (d[x], -x))

        return result
