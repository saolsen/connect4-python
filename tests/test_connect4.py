import connect4


def test_it():
    connect4.foo()
    assert True


def test_board_check():
    board: connect4.Board = (
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, "Red", None, None, None],
        [None, None, "Red", None, None, None],
        [None, None, "Blue", None, None, None],
        [None, None, "Red", None, None, None],
    )
    assert connect4.board_check(board) is None
    board: connect4.Board = (
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, "Red", None, None, None],
        [None, None, "Red", None, None, None],
        [None, None, "Red", None, None, None],
        [None, None, "Red", None, None, None],
    )
    assert connect4.board_check(board) == "Red"
    board: connect4.Board = (
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, "Blue", "Blue", "Blue", "Blue"],
        [None, None, "Red", None, None, None],
        [None, None, "Red", None, None, None],
        [None, None, "Red", None, None, None],
    )
    assert connect4.board_check(board) == "Blue"
