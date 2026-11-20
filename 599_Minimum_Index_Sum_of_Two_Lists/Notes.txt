class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        msi = float('inf')
        res = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    idx = i + j     
                    if idx < msi:
                        msi = idx
                        res = [list1[i]]
                    elif msi == idx:
                        res.append(list1[i])   
        return res