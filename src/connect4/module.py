from typing import Tuple, List


def foo():
    print("hello world")


Board = Tuple[
    List[None | str],
    List[None | str],
    List[None | str],
    List[None | str],
    List[None | str],
    List[None | str],
    List[None | str],
]


def turn(board: Board, color: str, column: int):
    assert 0 <= column < 7
    stack = board[column]
    for i, slot in enumerate(stack):
        if slot is None:
            stack[i] = color
            break


def board_display(board: Board):
    assert len(board) == 7
    for row in reversed(range(0, 6)):
        r = []
        for col in range(0, 7):
            e = board[col][row]
            if e is None:
                r.append(".")
            elif e == "Blue":
                r.append("B")
            elif e == "Red":
                r.append("R")
            else:
                assert False
        print(" ".join(r))


def board_check(board: Board):
    """
    See if anybody won yet.
    Just check in a dumb way for now.
    """
    # Check rows
    for row in range(0, 6):
        for col in range(0, 4):
            if (
                board[col][row] is not None
                and board[col][row]
                == board[col + 1][row]
                == board[col + 2][row]
                == board[col + 3][row]
            ):
                return board[col][row]
    # Check cols
    for col in range(0, 7):
        for row in range(0, 3):
            if (
                board[col][row] is not None
                and board[col][row]
                == board[col][row + 1]
                == board[col][row + 2]
                == board[col][row + 3]
            ):
                return board[col][row]

    # TODO: Diagonal
    return None
