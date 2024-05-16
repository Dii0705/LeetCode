class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        block = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    k = (i//3) * 3 + (j//3) # block index

                    rows[i][num] = rows[i].get(num,0)+1
                    cols[j][num] = cols[j].get(num,0)+1
                    block[k][num] = block[k].get(num,0) +1

                    if rows[i][num] > 1 or cols[j][num] > 1 or block[k][num] > 1:
                        return False
        return True
