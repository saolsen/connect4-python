import numpy as np

import random

from .game import State, Player


def rand_agent(board, player: Player, actions: list[int]) -> int:
    return random.choice(actions)


# Agent that plays connect4
# It does so by using montecarlo tree search to pick the best next move.
# The way it works is it simulates a bunch of random games for each of the
# moves it could pick. Whichever simulation did the best is the move it picks.
# This is done completely "on line" right now, so it's doing the simulations on it's
# turn.
def mcts_agent(board, player: Player, actions: list[int]) -> int:
    scores = {}
    for next_move in actions:
        # Rollout random games from this move.
        wins = 0
        losses = 0
        draws = 0

        for i in range(0, 100):
            state = State(
                board=np.array(board, copy=True),
                player=player,
            )
            state.turn(next_move)
            result, winner = state.play(rand_agent, rand_agent)
            if result == "DRAW":
                draws += 1
            elif result == "WIN":
                if winner == player:
                    wins += 1
                else:
                    losses += 1

        score = (wins * 1) + (losses * -1) / (wins + losses + draws)
        scores[next_move] = score

    # Pick the move that had the best win ratio in it's simulated games
    best_move = max(scores, key=scores.get)
    return best_move
