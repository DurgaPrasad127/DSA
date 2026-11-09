class Solution:
    def isArraySpecial(self, nums, queries):
        n = len(nums)
        bad = [0] * n

        # Build prefix sum
        for i in range(1, n):
            bad[i] = bad[i-1]

            if nums[i] % 2 == nums[i-1] % 2:
                bad[i] += 1

        # Answer queries
        res = []

        for l, r in queries:
            if bad[r] - bad[l] == 0:
                res.append(True)
            else:
                res.append(False)

        return res