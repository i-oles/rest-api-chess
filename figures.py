from abc import ABC, abstractmethod
import chess


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
        self.figure = "pawn"

    def list_available_moves(self):
        board = chess.Board(fen=None)
        field = chess.parse_square(self.current_field.lower())
        board.set_piece_at(field, chess.Piece.from_symbol("P"))
        return [board.san(move).capitalize()[:2] for move in board.legal_moves]

    def validate_move(self, dest_field):
        return dest_field.capitalize() in self.list_available_moves()


class Knight(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field
        self.figure = "knight"

    def list_available_moves(self):
        board = chess.Board(fen=None)
        field = chess.parse_square(self.current_field.lower())
        board.set_piece_at(field, chess.Piece.from_symbol("N"))
        return [board.san(move)[1:].capitalize() for move in board.legal_moves]

    def validate_move(self, dest_field):
        return dest_field.capitalize() in self.list_available_moves()


class Bishop(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field
        self.figure = "bishop"

    def list_available_moves(self):
        board = chess.Board(fen=None)
        field = chess.parse_square(self.current_field.lower())
        board.set_piece_at(field, chess.Piece.from_symbol("B"))
        return [board.san(move)[1:].capitalize() for move in board.legal_moves]

    def validate_move(self, dest_field):
        return dest_field.capitalize() in self.list_available_moves()


class Rook(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field
        self.figure = "rook"

    def list_available_moves(self):
        board = chess.Board(fen=None)
        field = chess.parse_square(self.current_field.lower())
        board.set_piece_at(field, chess.Piece.from_symbol("R"))
        return [board.san(move)[1:].capitalize() for move in board.legal_moves]

    def validate_move(self, dest_field):
        return dest_field.capitalize() in self.list_available_moves()


class Queen(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field
        self.figure = "queen"

    def list_available_moves(self):
        board = chess.Board(fen=None)
        field = chess.parse_square(self.current_field.lower())
        board.set_piece_at(field, chess.Piece.from_symbol("Q"))
        return [board.san(move)[1:].capitalize() for move in board.legal_moves]

    def validate_move(self, dest_field):
        return dest_field.capitalize() in self.list_available_moves()


class King(Figure):
    def __init__(self, current_field: str):
        self.current_field = current_field
        self.figure = "king"

    def list_available_moves(self):
        board = chess.Board(fen=None)
        field = chess.parse_square(self.current_field.lower())
        board.set_piece_at(field, chess.Piece.from_symbol("K"))
        return [board.san(move)[1:].capitalize() for move in board.legal_moves]

    def validate_move(self, dest_field):
        return dest_field.capitalize() in self.list_available_moves()
