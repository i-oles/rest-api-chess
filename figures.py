from abc import ABC, abstractmethod
import chess


class Figure(ABC):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self, piece_symbol, index_start=1, index_end=None):
        board = chess.Board(fen=None)
        try:
            field = chess.parse_square(self.current_field.lower())
            board.set_piece_at(field, chess.Piece.from_symbol(piece_symbol))
            
            return [board.san(move)[index_start:index_end].capitalize() for move in board.legal_moves]
        except ValueError:
            return []

    @abstractmethod
    def validate_move(self, dest_field: str):
        pass


class Pawn(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self):
        # return Figure.list_available_moves(self, "P", 0, 2)

        try:
            chess.parse_square(self.current_field.lower())
        except ValueError:
            return []

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
        return dest_field.capitalize() in self.list_available_moves()


class Knight(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self):
        return Figure.list_available_moves(self, "N")

    def validate_move(self, dest_field):
        return dest_field.capitalize() in self.list_available_moves()


class Bishop(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self):
        return Figure.list_available_moves(self, "B")

    def validate_move(self, dest_field):
        return dest_field.capitalize() in self.list_available_moves()


class Rook(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self):
        return Figure.list_available_moves(self, "R")

    def validate_move(self, dest_field):
        return dest_field.capitalize() in self.list_available_moves()


class Queen(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self):
        return Figure.list_available_moves(self, "Q")

    def validate_move(self, dest_field):
        return dest_field.capitalize() in self.list_available_moves()


class King(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self):
        return Figure.list_available_moves(self, "K")

    def validate_move(self, dest_field):
        return dest_field.capitalize() in self.list_available_moves()
