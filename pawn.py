from figure import Figure


class Pawn(Figure):
    def list_available_moves(self):
        letter = self.current_field[0].upper()
        rank = int(self.current_field[1:])
        if rank == 2:
            return [
                letter + str(rank + 1),
                letter + str(rank + 2)
                ]
        elif rank == 8:
            return []
        else:
            return [letter + str(rank + 1)]

    def validate_move(self, dest_field):
        pass