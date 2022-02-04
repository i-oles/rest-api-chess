"""
Ke5 = chess.Move.from_uci("e4e5")
board.push(Ke5)
print('************')
print(board)





# ex 1 - with base pieces positions 
board = chess.Board()
print(board)

print([move for move in board.legal_moves])


# ex 2 - for empty board
board = chess.Board(fen=None)
print(board)
board.set_piece_at(chess.E4, chess.Piece.from_symbol("p"))

print([move for move in board.legal_moves])
"""

import chess

# ex 3 - setting board manualy
board = chess.Board(fen='8/8/8/8/4B3/8/8/8 w - - 0 1')
print(board)

print([move for move in board.legal_moves])
