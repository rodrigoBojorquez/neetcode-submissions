class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        subbox_map = defaultdict(set)

        for col in range(len(board[0])):
            for row in range(len(board)):
                item = board[col][row]

                if item == ".":
                    continue

                if (item in row_map[row] or 
                item in col_map[col] or
                item in subbox_map[(row // 3) * 3 + (col // 3)]): 
                    return False

                row_map[row].add(item)
                col_map[col].add(item)
                subbox_map[(row // 3) * 3 + (col // 3)].add(item)

        return True