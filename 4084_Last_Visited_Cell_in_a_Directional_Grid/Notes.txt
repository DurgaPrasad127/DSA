class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])

        r = 0
        c = 0
        visited = set()

        while (r, c) not in visited:
            visited.add((r, c))

            if grid[r][c] == 'R':
                nc, nr = c + 1, r
            elif grid[r][c] == 'L':
                nc, nr = c - 1, r
            elif grid[r][c] == 'D':
                nc, nr = c, r + 1
            else:  # 'U'
                nc, nr = c, r - 1

            if nr < 0 or nr >= m or nc < 0 or nc >= n:
                break

            if (nr, nc) in visited:
                break

            r, c = nr, nc

        return [r, c]