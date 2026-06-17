class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num = board[i][j]
                    box_index = (i//3) + (j//3)*3
                    if num in rows[i] or num in columns[j] or num in boxes[box_index]:
                        return False
                    rows[i].add(num)
                    columns[j].add(num)
                    boxes[box_index].add(num)
        return True