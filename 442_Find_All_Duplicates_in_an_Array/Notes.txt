class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        count = {}

        dup = []
        for i in nums:
            if i in count:
                count[i] += 1
                dup.append(i)
            else:
                count[i] = 1
        
        return dup


        #for key,value in count.items():

