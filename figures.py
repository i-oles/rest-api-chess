from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, current_field: str, figure: str):
        self.current_field = current_field
        self.figure = figure

    @abstractmethod
    def list_available_moves(self):
        pass

    @abstractmethod
    def validate_move(self, dest_field: str):
        pass


class Pawn(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field
        self.figure = 'pawn'

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
        if dest_field.capitalize() in self.list_available_moves():
            return 'valid'
        else:
            return 'invalid'


class Knight(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field
        self.figure = 'knight'

    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        pass


class Bishop(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field
        self.figure = 'bishop'

    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        pass


class Rook(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field
        self.figure = 'rook'

    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        pass


class Queen(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field
        self.figure = 'queen'

    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        pass


class King(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field
        self.figure = 'king'

    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        pass







