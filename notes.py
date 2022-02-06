
import chess
"""

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



# ex 3 - setting board manualy
board = chess.Board(fen='8/8/8/8/4B3/8/8/8 w - - 0 1')
print(board)

print([move for move in board.legal_moves])

"""

board = chess.Board(fen=None)
board.set_piece_at(chess.E1, chess.Piece.from_symbol("P"))
print([board.lan(move) for move in board.legal_moves])
board.set_piece_at(chess.E7, chess.Piece.from_symbol("P"))
print([board.lan(move) for move in board.legal_moves])
board.set_piece_at(chess.E1, chess.Piece.from_symbol("N"))
print([board.lan(move) for move in board.legal_moves])

