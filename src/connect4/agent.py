import random

# Agent that plays connect4
# It does so by using montecarlo tree search to pick the best next move.
# The way it works is it simulates a bunch of random games for each of the
# moves it could pick. Whichever simulation did the best is the move it picks.
# This is done completely "on line" right now, so it's doing the simulations on it's
# turn.


# The policy can be anything, for example it could be
# this policy which just picks a random move.
def rand_agent() -> int:
    return random.randrange(0, 7)
