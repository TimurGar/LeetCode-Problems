
# Solved with HASH SET
# answer copied from online (pretty much everyone had done the same thing)

import collections

def isValidSudoku(board):
    # Usually, a Python dictionary throws a KeyError if you 
    # try to get an item with a key that is not currently in 
    # the dictionary. The defaultdict in contrast will simply 
    # create any items that you try to access (provided of course they do not exist yet).
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    boxes = collections.defaultdict(set) # key = (r // 3, c // 3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or 
                board[r][c] in columns[c] or
                board[r][c] in boxes[(r //3 , c // 3)]):
                return False
            
            rows[r].add(board[r][c])
            columns[c].add(board[r][c])
            boxes[(r //3 , c // 3)].add(board[r][c])

    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
    