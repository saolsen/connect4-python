from connect4 import State, Player
from connect4.agent import rand_agent, mcts_agent


def test_board_check():
    board = State()
    board.turn(Player.Blue, 2)
    board.display()
    board.turn(Player.Red, 3)
    board.display()
    board.turn(Player.Blue, 1)
    board.display()
    board.turn(Player.Red, 2)
    board.display()
    board.turn(Player.Blue, 0)
    board.display()
    board.turn(Player.Red, 0)
    board.display()
    board.turn(Player.Blue, 1)
    board.display()
    board.turn(Player.Red, 1)
    board.display()
    board.turn(Player.Blue, 0)
    board.display()
    result = board.turn(Player.Red, 0)

    assert result == Player.Red


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
