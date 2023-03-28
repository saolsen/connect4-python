from typing import Callable, Optional
from enum import Enum

import numpy as np

Player = Enum("Player", ["Blue", "Red"])
Slot = Optional[Player]

# Agent = Callable[[Board, Player, list[int]], int]


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
        if board is not None:
            self.board = board
        else:
            self.board = np.array(
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                ],
                dtype="i4",
            )
        if player is not None:
            self.player = player
        else:
            self.player = Player.Blue

    def _check(self):
        """
        See if anybody won yet.
        Just check in a dumb way for now, each possibility
        """
        # Check rows
        for row in range(0, 6):
            for col in range(0, 4):
                if (
                    self.board[col][row] != 0
                    and self.board[col][row]
                    == self.board[col + 1][row]
                    == self.board[col + 2][row]
                    == self.board[col + 3][row]
                ):
                    return ("WIN", self.board[col][row])
        # Check cols
        for col in range(0, 7):
            for row in range(0, 3):
                if (
                    self.board[col][row] != 0
                    and self.board[col][row]
                    == self.board[col][row + 1]
                    == self.board[col][row + 2]
                    == self.board[col][row + 3]
                ):
                    return ("WIN", self.board[col][row])
        # Check diag up
        for col in range(0, 4):
            for row in range(0, 3):
                if (
                    self.board[col][row] != 0
                    and self.board[col][row]
                    == self.board[col + 1][row + 1]
                    == self.board[col + 2][row + 2]
                    == self.board[col + 3][row + 3]
                ):
                    return ("WIN", self.board[col][row])

        # Check diag down
        for col in range(0, 4):
            for row in range(3, 6):
                if (
                    self.board[col][row] != 0
                    and self.board[col][row]
                    == self.board[col + 1][row - 1]
                    == self.board[col + 2][row - 2]
                    == self.board[col + 3][row - 3]
                ):
                    return ("WIN", self.board[col][row])

        # Check draw
        for col in range(0, 7):
            if self.board[col][5] == 0:
                # There are still moves left
                return None

        return ("DRAW", None)

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
