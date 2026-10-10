
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        abs_diff = []

        for i in range(len(nums1)):
            abs_diff.append(abs(nums1[i] - nums2[i]))

        k = k1 + k2

        if sum(abs_diff) <= k:
            return 0

        left = 0
        right = max(abs_diff)

        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in abs_diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        threshold = left

        operations = sum(max(0, d - threshold) for d in abs_diff)
        remaining = k - operations

        answer = 0

        for d in abs_diff:
            value = min(d, threshold)
            answer += value * value

        answer -= remaining * (2 * threshold - 1)

        return answer
