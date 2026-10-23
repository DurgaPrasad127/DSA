class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        res = -1
        min_capacity = float('inf')

        for i in range(len(capacity)):
            if capacity[i] >= itemSize and capacity[i] < min_capacity:
                min_capacity = capacity[i]
                res = i

        return res