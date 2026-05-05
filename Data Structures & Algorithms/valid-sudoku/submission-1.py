class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each row contains 1-9 without duplicates
        # each column contains 1-9 without duplicates
        # each 3x3 sub-box contains 1-9 without duplicates

        # defaultdict is a pretty usefull ds to avoid exceptions
        squares_map = defaultdict(set)
        columns_map = defaultdict(set)
        rows_map = defaultdict(set)

        for col in range(len(board[0])):
            for row in range(len(board)):
                item = board[row][col]

                if item == ".":
                    continue

                # validating column, row and square
                if (item in columns_map[col] or
                 item in rows_map[row] or
                 item in squares_map[(row // 3, col // 3)]):
                    return False
                    
                columns_map[col].add(item)
                rows_map[row].add(item)
                squares_map[(row // 3, col // 3)].add(item)
            
        return True