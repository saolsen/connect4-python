import random

from connect4 import State, Player, InvalidMove


# Dumbest agent possible, has no idea what is going on, just picks
# a random column
def rand_agent() -> int:
    return random.randrange(0, 7)


def next_player(player: Player):
    if player == player.Blue:
        return player.Red
    return player.Blue


def play():
    state = State()
    player = Player.Blue

    print("Connect4")
    print("Blue Goes First (that's you)")
    print("Enter the column to drop a chip into")
    while True:
        state.display()

        if player == Player.Blue:
            move = int(input(f"{player.name}'s move: "))
            try:
                result = state.turn(player, move)
            except InvalidMove as e:
                print("Invalid Move:", e)
                continue
        else:
            while True:
                move = rand_agent()
                try:
                    result = state.turn(player, move)
                except InvalidMove:
                    # Just try again, chances are next rand move is fine.
                    continue
                break

        if result is not None:
            state.display()
            print(f"{result.name} wins!")
            break

        player = next_player(player)


if __name__ == "__main__":
    try:
        play()
    except (KeyboardInterrupt, EOFError):
        exit()
