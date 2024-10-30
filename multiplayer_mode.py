from gameplay import Gameplay


class MultiPlayer(Gameplay):

    def __init__(self):
        super().__init__()

    def check_turn(self):
        if self.round_counter % 2 == 0:
            self.make_move(player="Player 1", mark="x")
        else:
            self.make_move(player="Player 2", mark="o")
        self.round_counter += 1

    def make_move(self, **kwargs):

        player = kwargs.get('player')
        mark = kwargs.get('mark')

        player_move = input(f"{player} choose block number to mark: ")

        if player_move.isnumeric():
            player_move = int(player_move)
        else:
            print("this is not an option, choose again")
            return self.make_move(**kwargs)

        if player_move in self.allowed_moves:
            self.block_dict[player_move] = mark
            self.allowed_moves.remove(player_move)
        else:
            print("this is not an option, choose again")
            return self.make_move(**kwargs)


