class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        minus = []
        plus = []

        for num in nums:
            if num <= 0:
                minus.append(num)
            if num >= 0:
                plus.append(num)

        minus.sort()
        plus.sort()

        mp = []

        # Three largest numbers when all numbers are negative
        if len(plus) == 0:
            mp.append(minus[-1] * minus[-2] * minus[-3])

        # Three largest numbers when all numbers are positive
        if len(minus) == 0:
            mp.append(plus[-1] * plus[-2] * plus[-3])

        # Two smallest numbers and the largest number
        if len(minus) >= 2 and len(plus) >= 1:
            mp.append(minus[0] * minus[1] * plus[-1])

        # Three largest numbers
        if len(plus) >= 3:
            mp.append(plus[-1] * plus[-2] * plus[-3])

        return max(mp) if mp else 0

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()

        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]

        return max(a, b)