from gameplay import Gameplay
import random


class Computer(Gameplay):

    def __init__(self):
        super().__init__()

    def make_move(self):
        if self.round_counter % 2 == 0:
            player_move = input("Choose block number to mark: ")

            if player_move.isnumeric():
                player_move = int(player_move)
            else:
                print("this is not an option, choose again")
                return self.make_move()

            if player_move in self.allowed_moves:
                self.block_dict[player_move] = "x"
                self.allowed_moves.remove(player_move)
            else:
                print("this is not an option, choose again")
                return self.make_move()
        else:
            print("Computer's play:")
            computer_move = random.choice(self.allowed_moves)
            self.block_dict[computer_move] = "o"
            self.allowed_moves.remove(computer_move)
        self.round_counter += 1

