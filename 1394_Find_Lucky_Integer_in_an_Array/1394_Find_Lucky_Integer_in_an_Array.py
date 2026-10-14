class Solution:
    def findLucky(self, arr: list[int]) -> int:
        count = {}

        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        li = -1
        for key,value in count.items():
            if key == value and key > li:
                li = key
        
        return li
                
        

        
        