class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        res = []
        for i in range(len(matrix[0])):
            ans = []
            for j in range(len(matrix)):
                ans.append(matrix[j][i])
            res.append(ans)
        return res