class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # we want to traverse grid2, and grid1 at the same time
        m = len(grid1)
        n = len(grid1[0])

        def remove_non_common(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid2[r][c]==0:
                return

            # reset to 0
            grid2[r][c] = 0

            remove_non_common(r+1, c)
            remove_non_common(r-1, c)
            remove_non_common(r, c+1)
            remove_non_common(r, c-1)

        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and grid1[row][col]==0:
                    remove_non_common(row, col)
        count = 0
        # now count how many sub-islands are there
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1:
                    remove_non_common(row, col)
                    count +=1

        return count