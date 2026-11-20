class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        diff = (sum(bobSizes) - sum(aliceSizes)) // 2
        bob_set = set(bobSizes)

        for x in aliceSizes:
            if x + diff in bob_set:
                return [x,x+diff]