from connect4 import State, Player
from connect4.agent import rand_agent, mcts_agent


# NOTE: This takes a long time because my code is all slow still.
def test_vs_random():
    """
    If the mcts bot is any good than surely it wont ever lose to the random bot
    """
    for game in range(0, 10):
        state = State()
        result, winner = state.play(mcts_agent, rand_agent)
        if result == "WIN":
            assert winner == Player.Blue
