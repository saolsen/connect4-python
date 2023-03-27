# Really simple program to play connect4 against yourself.
from connect4 import State, Board, Player, display


def play():
    state = State()
    print("Connect4")
    print("Blue Goes First")
    print("Enter the column to drop a chip into")

    def agent(board: Board, player: Player) -> int:
        display(board)
        move = int(input(f"{player.name}'s move: "))
        return move

    result = state.play(agent, agent)
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
