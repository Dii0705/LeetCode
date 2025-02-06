class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def remove_boundary_connected_land(r,c):
            # Out of Bounds
            if r<0 or c<0 or r>=ROWS or c>= COLS or (r,c) in visited:
                return 0
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            remove_boundary_connected_land(r+1,c)
            remove_boundary_connected_land(r-1,c)
            remove_boundary_connected_land(r,c+1)
            remove_boundary_connected_land(r,c-1)

        for row in range(ROWS):
            for col in range(COLS):
                # lands of boundary 
                if grid[row][col] == 1 and (
                    row in [0, ROWS-1] or col in [0, COLS-1]
                ):
                    remove_boundary_connected_land(row, col)

        # count the rest lands
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count += 1
        return count
        

