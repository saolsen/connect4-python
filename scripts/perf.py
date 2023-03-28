from connect4 import State
from connect4.agent import rand_agent, mcts_agent


def play():
    for _ in range(0, 10):
        state = State()
        state.play(mcts_agent, rand_agent)


if __name__ == "__main__":
    play()
