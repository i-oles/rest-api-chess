from figures import Pawn, Knight, Bishop, Rook, Queen, King

from flask import Flask

"""
bugs:
1. pawn promotion -> ex. 4 x D8
2. pawn: a8 -> zwraca error null, albo error field does not exist
3. pawn: a1 --> zwraca a2, a3
4. pawn on a1 never stands - ?
5. testing abstrac method? correct?
6. abstract method - correct?
7. figure uppercase not allowed
8. status codes correct

questions:
7. test create_king c7 -> C7 is ok?
8. second GET - 'field does not exist' - is it necessary?
9. 'move' can be hardcoded?
10. 'validate_moves' should return bool?
11. should I validate dest_field
12. comments?
13. pytest?

1. flake8 - line 68 too long
2. pip freeze -> too many imports?
3. imports in tests folder
4. in readme only valid cases?


todo:
1. security
2. validate response status codes

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


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def get_available_moves(chess_figure, current_field):

    piece = figures[chess_figure](current_field)

    if piece.list_available_moves():
        error = None
    else:
        error = "Field does not exist."

    return {
        "availableMoves": piece.list_available_moves(),
        "error": error,
        "figure": chess_figure,
        "currentField": current_field.capitalize(),
    }


@app.route(
    "/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"]
)  # noqa: E501
def get_validate_move(chess_figure, current_field, dest_field):

    piece = figures[chess_figure](current_field)

    if piece.validate_move(dest_field):
        move = "valid"
        error = None
    else:
        move = "invalid"
        error = "Current move is not permitted."

    return {
        "move": move,
        "figure": chess_figure,
        "error": error,
        "currentField": current_field.capitalize(),
        "destField": dest_field.capitalize(),
    }


if __name__ == "__main__":
    app.run(debug=True)
