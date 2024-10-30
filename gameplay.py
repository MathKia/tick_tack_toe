import random


class Gameplay:

    def __init__(self):
        self.block_dict = {
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9"
        }
        self.round_counter = 0
        self.allowed_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def game_grid(self):
        print(f"{self.block_dict[1]} | {self.block_dict[2]} | {self.block_dict[3]}\n"
              f"_________\n"
              f"{self.block_dict[4]} | {self.block_dict[5]} | {self.block_dict[6]}\n"
              f"_________\n"
              f"{self.block_dict[7]} | {self.block_dict[8]} | {self.block_dict[9]}\n")

    def check_rules(self, player1, player2):
        conditions = [[self.block_dict[1], self.block_dict[2], self.block_dict[3]],
                      [self.block_dict[4], self.block_dict[5], self.block_dict[6]],
                      [self.block_dict[7], self.block_dict[8], self.block_dict[9]],
                      [self.block_dict[1], self.block_dict[5], self.block_dict[9]],
                      [self.block_dict[7], self.block_dict[5], self.block_dict[3]],
                      [self.block_dict[1], self.block_dict[4], self.block_dict[7]],
                      [self.block_dict[2], self.block_dict[5], self.block_dict[8]],
                      [self.block_dict[3], self.block_dict[6], self.block_dict[9]],
                      ]
        for condition in conditions:
            if condition[0] == condition[1] == condition[2]:
                winner = condition[0]
                if winner == "x":
                    print(f"Game Over: {player1} won!")
                else:
                    print(f"Game Over: {player2} won!")
                return True

        if len(self.allowed_moves) == 0:
            print("Game Over: Its a draw!")
            return True
