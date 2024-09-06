class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r,c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] == 0 or
                (r,c) in visit
            ):
                return 0
            visit.add((r,c))
            
            area = 1
            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)

            # we are not removing (r,c) from visit 
            # cuz we don't care about the permutation
            return area

        area = 0
        for row in range(ROWS):
            for col in range(COLS):
                area = max(area,dfs(row,col))
        return area