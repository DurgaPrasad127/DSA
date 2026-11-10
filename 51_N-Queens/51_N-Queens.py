class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        visited = set()
        leftdia = set()
        rightdia = set()

        solutions = []
        board = [["."] * n for _ in range(n)]

        def place(i):
            if i == n:
                solutions.append(["".join(row) for row in board])
                return

            for j in range(n):
                if (j in visited or
                    (i - j) in leftdia or
                    (i + j) in rightdia):
                    continue

                # Place queen
                visited.add(j)
                leftdia.add(i - j)
                rightdia.add(i + j)
                board[i][j] = "Q"

                # Recursive call
                place(i + 1)

                # Backtracking
                visited.remove(j)
                leftdia.remove(i - j)
                rightdia.remove(i + j)
                board[i][j] = "."

        place(0)
        return solutions