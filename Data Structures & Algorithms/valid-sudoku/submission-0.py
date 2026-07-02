class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    if num in rows[r]:
                        return False
                    if num in cols[c]:
                        return False
                    
                    b = (r // 3 * 3 + c // 3)
                    if num in boxes[b]:
                        return False
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)
        return True

