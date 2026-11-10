class Solution:
    def totalNQueens(self, n: int) -> int:

        visited = set()
        leftdia = set()
        rightdia = set()

        count = 0

        def place(i):
            nonlocal count

            if i == n:
                count += 1
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

                # Recursive call
                place(i + 1)

                # Backtracking
                visited.remove(j)
                leftdia.remove(i - j)
                rightdia.remove(i + j)

        place(0)

        return count