class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        ccs = 0
        for i in range(len(nums)):
            curr = nums[i]
            mn = nums[i]

            for j in range(i,len(nums)):
                curr &= nums[j]
                mn = min(mn, nums[j])

                if curr == mn:
                    ccs += 1

        return ccs