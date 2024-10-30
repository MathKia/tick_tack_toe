from multiplayer_mode import MultiPlayer
from computer_mode import Computer

computer = Computer()
multi = MultiPlayer()


def game_on():
    mode = input("Play Computer (C) or Player (P): \n").upper()
    if mode == "C":
        computer.game_grid()
        while len(computer.allowed_moves) > 0:
            computer.make_move()
            computer.game_grid()
            if computer.check_rules(player1="You", player2="Computer"):
                break
    elif mode == "P":
        multi.game_grid()
        while len(multi.allowed_moves) > 0:
            multi.check_turn()
            multi.game_grid()
            if multi.check_rules(player1="Player 1", player2="Player 2"):
                break
    else:
        print("this is not an option. retry")
        return game_on()


game_on()


