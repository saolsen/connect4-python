from typing import Callable, Optional
from enum import Enum

import numpy as np
from numba import njit

Player = Enum("Player", ["Blue", "Red"])
Slot = Optional[Player]

# Agent = Callable[[Board, Player, list[int]], int]


@njit()
def _fast_check(board):
    # Check rows
    for row in range(0, 6):
        for col in range(0, 4):
            if (
                board[col][row] != 0
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
                board[col][row] != 0
                and board[col][row]
                == board[col][row + 1]
                == board[col][row + 2]
                == board[col][row + 3]
            ):
                return board[col][row]
    # Check diag up
    for col in range(0, 4):
        for row in range(0, 3):
            if (
                board[col][row] != 0
                and board[col][row]
                == board[col + 1][row + 1]
                == board[col + 2][row + 2]
                == board[col + 3][row + 3]
            ):
                return board[col][row]

    # Check diag down
    for col in range(0, 4):
        for row in range(3, 6):
            if (
                board[col][row] != 0
                and board[col][row]
                == board[col + 1][row - 1]
                == board[col + 2][row - 2]
                == board[col + 3][row - 3]
            ):
                return board[col][row]

    # Check draw
    for col in range(0, 7):
        if board[col][5] == 0:
            # There are still moves left
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
            s: Slot = board[col][row]
            if s == 0:
                r.append(".")
            elif s == 1:
                r.append(f"{BLUE}B{END}")
            elif s == 2:
                r.append(f"{RED}R{END}")
            else:
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
        actions = []
        for col in range(0, 7):
            if self.board[col][5] == 0:
                actions.append(col)
        return actions

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
