from enum import Enum

import numpy as np
from numba import njit  # type: ignore

Player = Enum("Player", ["Blue", "Red"])


@njit(inline="always")
def _check_run(arr):
    """
    Check for a run of 4
    """
    p = 0
    n = 0
    for i in range(len(arr)):
        if arr[i] == p:
            n += 1
        else:
            p = arr[i]
            n = 1

        if n == 4 and p != 0:
            return p


@njit(cache=True)
def _fast_check(board):
    # Check rows
    for row in range(0, 6):
        check = _check_run(board[:, row])
        if check is not None:
            return check

    # Check cols
    for col in range(0, 7):
        check = _check_run(board[col])
        if check is not None:
            return check

    # Check diagonals
    for o in range(-3, 3):
        check = _check_run(np.diag(board, k=o))
        if check is not None:
            return check

    fb = np.fliplr(board)
    for o in range(-3, 3):
        check = _check_run(np.diag(fb, k=-o))
        if check is not None:
            return check

    # Check draw
    if np.all(board[:, 5] == 0):
        return 0

    return 3  # draw


class InvalidMove(Exception):
    pass


BLUE = "\033[94m"
RED = "\033[91m"
END = "\033[0m"


def display(board):
    print("0 1 2 3 4 5 6")
    for row in reversed(range(0, 6)):
        r = []
        for col in range(0, 7):
            s = board[col][row]
            match s:
                case 0:
                    r.append(".")
                case 1:
                    r.append(f"{BLUE}B{END}")
                case 2:
                    r.append(f"{RED}R{END}")
                case _:
                    assert False
        print(" ".join(r))


class State:
    def __init__(self, board=None, player=None):
        self.board = np.zeros((7, 6), dtype="i") if board is None else board
        self.player = Player.Blue if player is None else player

    def _check(self):
        """
        See if anybody won yet.
        Just check in a dumb way for now, each possibility
        """
        results = [None, ("WIN", Player.Blue), ("WIN", Player.Red), ("DRAW", None)]
        result = _fast_check(self.board)
        return results[result]

    def actions(self):
        return list(np.where(self.board[:, 5] == 0)[0])

    def turn(self, column: int):
        stack = self.board[column]

        for i, slot in enumerate(stack):
            if slot == 0:
                stack[i] = self.player.value
                break

        if self.player == Player.Blue:
            self.player = Player.Red
        else:
            self.player = Player.Blue

        return self._check()

    def play(self, blue, red):
        agents = {Player.Blue: blue, Player.Red: red}

        while True:
            actions = self.actions()
            move = agents[self.player](self.board, self.player, actions)
            assert move in actions
            result = self.turn(move)

            if result is not None:
                return result
