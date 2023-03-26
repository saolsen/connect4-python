# Really simple program to play connect for against yourself.
from connect4 import State, Player, InvalidMove


def next_player(player: Player):
    if player == player.Blue:
        return player.Red
    return player.Blue


def play():
    state = State()
    player = Player.Blue

    print("Connect4")
    print("Blue Goes First")
    print("Enter the column to drop a chip into")
    while True:
        state.display()
        move = int(input(f"{player.name}'s move: "))
        try:
            result = state.turn(player, move)
        except InvalidMove as e:
            print("Invalid Move:", e)
            continue

        if result is not None:
            print(f"{result.name} wins!")
            break

        player = next_player(player)


if __name__ == "__main__":
    try:
        play()
    except (KeyboardInterrupt, EOFError):
        exit()
