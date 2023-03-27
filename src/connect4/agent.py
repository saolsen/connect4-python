import random
from copy import deepcopy

from .game import State, Board, Player


def rand_agent(board: Board, player: Player) -> int:
    return random.randrange(0, 7)


# Agent that plays connect4
# It does so by using montecarlo tree search to pick the best next move.
# The way it works is it simulates a bunch of random games for each of the
# moves it could pick. Whichever simulation did the best is the move it picks.
# This is done completely "on line" right now, so it's doing the simulations on it's
# turn.
def mcts_agent(board: Board, player: Player) -> int:
    scores = []
    for next_move in range(0, 7):
        # Rollout random games from this move.
        wins = 0
        losses = 0
        draws = 0

        for i in range(0, 50):
            state = State(
                board=deepcopy(board),
                player=deepcopy(player),
            )
            state.turn(player, next_move)
            result, winner = state.play(rand_agent, rand_agent)
            if result == "DRAW":
                draws += 1
            elif result == "WIN":
                if winner == player:
                    wins += 1
                else:
                    losses += 1

        score = (wins * 1) + (losses * -1) / (wins + losses + draws)
        scores.append(score)

    # Pick the move that had the best win ratio in it's simulated games
    best_move = scores.index(max(scores))
    return best_move
