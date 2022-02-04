from figures import Figure, Pawn, Knight, Bishop, Rook, Queen, King

from flask import Flask
import chess

"""
todo:
1. pawn: a8 -> zwraca error null
2. implement validate_move() for each figure using chess lib
3. implement route validate moves
4. implement get_available_moves for rest pieces
5. make tests
6. security
7. validate response codes
8. write readme.md
9. install Black
10. install flake8


"""

app = Flask(__name__)


figures = {
    'pawn': Pawn,
    'knight': Knight,
    'bishop': Bishop,
    'rook': Rook,
    'queen': Queen,
    'king': King
}


def field_exist(current_field):
    try:
        chess.parse_square(current_field)
    except ValueError:
        return False
   

def json_validate_move(cls, current_field, chess_figure, dest_field):
    piece = cls(current_field)
    if field_exist(current_field) == False:
        move = piece.validate_move(dest_field)
        return {
            'move': move,
            "figure": chess_figure,
            "error": 'Current move is not permitted',
            "currentField": current_field.capitalize(),
            "destField": dest_field.capitalize()
            }
    else:
        move = piece.validate_move(dest_field)
        return {
            'move': move,
            "figure": chess_figure,
            "error": 'null',
            "currentField": current_field.capitalize(),
            "destField": dest_field.capitalize()
            }


def json_available_moves(cls, current_field, chess_figure):
    piece = cls(current_field)
    if field_exist(current_field) == False:
        return {
            'availableMoves': [],
            "error": 'Field does not exist',
            "figure": chess_figure,
            "currentField": current_field.capitalize()
            }
    else:
        available_moves = piece.list_available_moves()
        return {
            'availableMoves': available_moves,
            "error": 'null',
            "figure": chess_figure,
            "currentField": current_field.capitalize()
            }




@app.route("/api/v1/<chess_figure>/<current_field>", methods=['GET'])
def get_available_moves(chess_figure, current_field):
    if chess_figure == 'pawn':
        return json_available_moves(Pawn, current_field, chess_figure)
    

@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=['GET'])
def validate_move(chess_figure, current_field, dest_field):
    if chess_figure == 'pawn':
        return json_validate_move(Pawn, current_field, chess_figure, dest_field)




if __name__ == '__main__':
    app.run(debug=True)

