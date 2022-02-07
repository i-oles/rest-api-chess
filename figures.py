from abc import ABC, abstractmethod
import chess

"""
Functions validate_move() and list_available_moves()
were implemented due to the need to define an abstract class,
otherwise they would be implemented in parent class: Figure
"""


def validate_move(available_moves: list, dest_field: str) -> bool:
    if available_moves is not None:
        return dest_field.capitalize() in available_moves
    else:
        return False


def list_available_moves(
    current_field: str, piece_symbol: str, i_start=1, i_end=None
) -> list or None:
    board = chess.Board(fen=None)
    try:
        field = chess.parse_square(current_field.lower())
        board.set_piece_at(field, chess.Piece.from_symbol(piece_symbol))
        return [
            board.san(move)[i_start:i_end].capitalize() for move in board.legal_moves
        ]
    except ValueError:
        return None


class Figure(ABC):
    def __init__(self, current_field: str):
        self.current_field = current_field

    @abstractmethod
    def list_available_moves(self) -> list:
        pass

    @abstractmethod
    def validate_move(self, dest_field: str) -> bool:
        pass


"""
pawn is irregular case:
1. it never stands on first rank (I assumed -> one square forward)
2. due to chess rules from rank 2 pawn can move one or two squares forward
3. chess python lib take into account the pawn promotions from 7th rank (4 move options)
(I assumed -> one square forward, without promotion adnotations)
4. it never stands on 8th rank because of promotion
(I assumed -> it can stand but without move possibility)

"""


class Pawn(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self) -> list:
        letter = self.current_field[0].upper()
        rank = self.current_field[1:]

        if rank == "1":
            return [f"{letter}2"]
        elif rank == "7":
            return list(set(list_available_moves(self.current_field, "P", 0, 2)))
        else:
            return list_available_moves(self.current_field, "P", 0)

    def validate_move(self, dest_field) -> bool:
        return validate_move(self.list_available_moves(), dest_field)


class Knight(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self) -> list:
        return list_available_moves(self.current_field, "N")

    def validate_move(self, dest_field) -> bool:
        return validate_move(self.list_available_moves(), dest_field)


class Bishop(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self) -> list:
        return list_available_moves(self.current_field, "B")

    def validate_move(self, dest_field) -> bool:
        return validate_move(self.list_available_moves(), dest_field)


class Rook(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self) -> list:
        return list_available_moves(self.current_field, "R")

    def validate_move(self, dest_field) -> bool:
        return validate_move(self.list_available_moves(), dest_field)


class Queen(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self) -> list:
        return list_available_moves(self.current_field, "Q")

    def validate_move(self, dest_field) -> bool:
        return validate_move(self.list_available_moves(), dest_field)


class King(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field

    def list_available_moves(self) -> list:
        return list_available_moves(self.current_field, "K")

    def validate_move(self, dest_field) -> bool:
        return validate_move(self.list_available_moves(), dest_field)
