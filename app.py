from figures import Pawn, Knight, Bishop, Rook, Queen, King

from flask import Flask
import chess

"""
bugs:
1. nothing works on a1
2. pawn promotion -> ex. 4 x D8
3. 'move' can be hardcoded?
4. null is not in quotes in decription
5. second GET - 'field does not exist' - is it necessary?
6. flake8 - line 68 too long
7. pip freeze -> too many imports
8. code does not work when upppercase letters
9. available_moves -> two dicts?
10. field validation - the best way?
11. pawn: a8 -> zwraca error null

todo:
2. move methods to abstract method - make all classes shorter
3. make tests
4. security
5. validate response codes
6. write readme.md

"""

app = Flask(__name__)


figures = {
    "pawn": Pawn,
    "knight": Knight,
    "bishop": Bishop,
    "rook": Rook,
    "queen": Queen,
    "king": King,
}


def field_exist(current_field):
    try:
        return chess.parse_square(current_field)
    except ValueError:
        return False


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def get_available_moves(chess_figure, current_field):

    piece = figures[chess_figure](current_field)
    if field_exist(current_field) is False:
        return {
            "availableMoves": [],
            "error": "Field does not exist.",
            "figure": chess_figure,
            "currentField": current_field.capitalize(),
        }
    else:
        available_moves = piece.list_available_moves()
        return {
            "availableMoves": available_moves,
            "error": "null",
            "figure": chess_figure,
            "currentField": current_field.capitalize(),
        }


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
def validate_move(chess_figure, current_field, dest_field):

    piece = figures[chess_figure](current_field)

    if field_exist(current_field) and field_exist(dest_field):
        if piece.validate_move(dest_field):
            error = "null"
            move = "valid"
        else:
            move = "invalid"
            error = "Current move is not permitted."
    else:
        move = "invalid"
        error = "Field does not exist."

    return {
        "move": move,
        "figure": chess_figure,
        "error": error,
        "currentField": current_field.capitalize(),
        "destField": dest_field.capitalize(),
    }


if __name__ == "__main__":
    app.run(debug=True)
