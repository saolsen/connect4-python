from connect4 import State, Player


def test_board_check():
    board = State()
    board.turn(Player.Blue, 2)
    board.display()
    board.turn(Player.Red, 3)
    board.display()
    board.turn(Player.Blue, 1)
    board.display()
    board.turn(Player.Red, 2)
    board.display()
    board.turn(Player.Blue, 0)
    board.display()
    board.turn(Player.Red, 0)
    board.display()
    board.turn(Player.Blue, 1)
    board.display()
    board.turn(Player.Red, 1)
    board.display()
    board.turn(Player.Blue, 0)
    board.display()
    result = board.turn(Player.Red, 0)

    assert result == Player.Red
