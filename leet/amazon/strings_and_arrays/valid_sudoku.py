from typing import List


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3 # note how we are getting the index of the box

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def OK(arr):
            for a in arr:
                digits_only = list(filter(str.isdigit, a))
                if len(digits_only) != len(set(digits_only)):
                    return False
            return True

        if not OK(board) or not OK(zip(*board)):
            return False

        for i in (0, 3, 6):
            for j in (0, 3, 6):
                temp = []
                for offset in range(3):
                    temp.extend(board[i + offset][j:j + 3])
                    digits_only = list(filter(str.isdigit, temp))
                    if len(digits_only) != len(set(digits_only)):
                        return False
        return True
