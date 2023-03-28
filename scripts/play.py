# Play connect4 against yourself or an agent
import sys

from connect4 import State, Player, display, BLUE, RED, END
from connect4.agent import rand_agent, mcts_agent

names = {Player.Blue: f"{BLUE}Blue{END}", Player.Red: f"{RED}Red{END}"}


def cli_agent(board, player: Player, actions: list[int]) -> int:
    while True:
        display(board)
        move = int(input(f"{names[player]}'s move: "))
        if move in actions:
            return move
        else:
            print("Invalid Column")


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
        print(f"{names[winner]} WINS!")


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
