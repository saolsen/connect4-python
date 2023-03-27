from typing import Callable, Optional
from enum import Enum

Player = Enum("Player", ["Red", "Blue"])
Slot = Optional[Player]

# TODO: probably make this a numpy array
Board = tuple[
    list[Slot], list[Slot], list[Slot], list[Slot], list[Slot], list[Slot], list[Slot]
]

Agent = Callable[[Board, Player], int]


class InvalidMove(Exception):
    pass


BLUE = "\033[94m"
RED = "\033[91m"
END = "\033[0m"


def display(board: Board):
    print("0 1 2 3 4 5 6")
    for row in reversed(range(0, 6)):
        r = []
        for col in range(0, 7):
            s: Slot = board[col][row]
            if s is None:
                r.append(".")
            elif s == Player.Blue:
                r.append(f"{BLUE}B{END}")
            elif s == Player.Red:
                r.append(f"{RED}R{END}")
            else:
                assert False
        print(" ".join(r))


class State:
    def __init__(self, board=None, player=None):
        if board is not None:
            self.board = board
        else:
            self.board: Board = (
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
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
                    self.board[col][row] is not None
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
                    self.board[col][row] is not None
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
                    self.board[col][row] is not None
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
                    self.board[col][row] is not None
                    and self.board[col][row]
                    == self.board[col + 1][row - 1]
                    == self.board[col + 2][row - 2]
                    == self.board[col + 3][row - 3]
                ):
                    return ("WIN", self.board[col][row])

        # Check draw
        for col in range(0, 7):
            if self.board[col][5] is None:
                # There are still moves left
                return None

        return ("DRAW", None)

    def turn(self, player: Player, column: int):
        if player != self.player:
            raise InvalidMove(f"It is {self.player.name}'s turn")
        if column < 0 or column > 6:
            raise InvalidMove(f"No column {column}")
        stack = self.board[column]
        if stack[5] is not None:
            raise InvalidMove(f"Column {column} is Full")
        for i, slot in enumerate(stack):
            if slot is None:
                stack[i] = player
                break

        if self.player == player.Blue:
            self.player = player.Red
        else:
            self.player = player.Blue

        return self._check()

    def play(self, blue: Agent, red: Agent):
        while True:
            if self.player == Player.Blue:
                agent = blue
            else:
                agent = red

            while True:
                try:
                    move = agent(self.board, self.player)
                    result = self.turn(self.player, move)
                except InvalidMove:
                    # TODO: probably don't wanna print here.
                    # print("Invalid Move")
                    continue
                break

            if result is not None:
                return result
