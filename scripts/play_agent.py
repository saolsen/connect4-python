import random
from connect4 import State, Board, Player, display


def play():
    state = State()
    print("Connect4")
    print("Blue Goes First")
    print("Enter the column to drop a chip into")

    def player_agent(board: Board, player: Player) -> int:
        display(board)
        move = int(input(f"{player.name}'s move: "))
        return move

    def random_agent(board, player) -> int:
        return random.randrange(0, 7)

    result = state.play(player_agent, random_agent)
    display(state.board)
    if result is None:
        print("DRAW!")
    else:
        print(f"{result.name} WINS!")


if __name__ == "__main__":
    try:
        play()
    except (KeyboardInterrupt, EOFError):
        exit()
