import chess

field = 'b3'

index = chess.parse_square(field)
letter = chess.square_file(index)
print(letter)