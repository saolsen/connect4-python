import connect4

# Connect 4 is played on a board like this.
# O O O O O O O
# O O O O O O O
# O O O O O O O
# O O O O O O O
# O O O O O O O
# O O O O O O O

# When it's your turn you can put your color (Red or Blue) in one of the columns.
# A simple data structure for the board would be an array of 7 stacks of 6 items.
board: connect4.Board = (
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
)


connect4.turn(board, "Blue", 2)
connect4.turn(board, "Red", 3)
connect4.turn(board, "Blue", 1)
connect4.turn(board, "Red", 2)


connect4.board_display(board)
print(connect4.board_check(board))
