# Play connect4 against yourself or an agent
import sys

from connect4 import State, Board, Player, display
from connect4.agent import rand_agent, mcts_agent


def cli_agent(board: Board, player: Player) -> int:
    display(board)
    move = int(input(f"{player.name}'s move: "))
    return move


def play(agent=cli_agent):
    state = State()
    print("Connect4")
    print("Blue Goes First")
    print("Enter the column to drop a chip into")

    result, winner = state.play(cli_agent, agent)
    display(state.board)
    print(result)
    if result == "DRAW":
        print("DRAW!")
    elif result == "WIN":
        print(f"{winner.name} WINS!")


agents = {"rand_agent": rand_agent, "mcts_agent": mcts_agent}

if __name__ == "__main__":
    if len(sys.argv) == 2:
        agent = agents[sys.argv[1]]
    else:
        agent = cli_agent
    try:
        play(agent)
    except (KeyboardInterrupt, EOFError):
        exit()
