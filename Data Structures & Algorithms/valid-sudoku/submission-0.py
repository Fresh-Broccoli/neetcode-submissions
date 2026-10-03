class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        v_grid, g_grid = [{} for _ in range(len(board))], [[{} for _ in range(int(len(board)/3))] for _ in range(int(len(board)/3))]
        for i in range(len(board)):
            h_d = {}
            for j in range(len(board)):
                n = board[i][j]
                if n != ".":
                    # Horizontal check
                    if n not in h_d:
                        h_d[n] = 1
                    else:
                        return False

                    # Vertical check
                    if n not in v_grid[j]:
                        v_grid[j][n] = 1
                    else:
                        return False

                    # Grid check
                    i_g, j_g = int(i/3), int(j/3)
                    if n not in g_grid[i_g][j_g]:
                        g_grid[i_g][j_g][n] = 1
                    else:
                        return False

        return True