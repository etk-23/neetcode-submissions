class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # go box by box
        for box in range(9):

            start_row = (box // 3) * 3
            start_col = (box % 3) * 3

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):

                    val = board[i][j]

                    # ignore blank squares
                    if val == ".":
                        continue

                    # check row, column and current box
                    if (
                        val in rows[i]
                        or val in cols[j]
                        or val in boxes[box]
                    ):
                        return False

                    # remember the given value
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[box].add(val)

        return True