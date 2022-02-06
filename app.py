from figures import Pawn, Knight, Bishop, Rook, Queen, King

from flask import Flask

"""
bugs:
X1. pawn promotion -> ex. 4 x D8
X2. pawn: a8 -> zwraca error null, albo error field does not exist
X3. pawn: a1 --> zwraca a2, a3
X4. pawn on a1 never stands - ?
5. testing abstrac method? correct?
X6. abstract method - correct?
7. status codes correct? where 500?
8. status 404 -> return whole dict of just error
9. test 500 status

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
    if chess_figure not in figures:
        return {"error": "Figure does not exist."}, 404

    piece = figures[chess_figure](current_field)
    if piece.list_available_moves():
        return {
            "availableMoves": piece.list_available_moves(),
            "error": None,
            "figure": chess_figure,
            "currentField": current_field.capitalize(),
        }, 200 
    else:
        return {
            "availableMoves": piece.list_available_moves(),
            "error": "Field does not exist.",
            "figure": chess_figure,
            "currentField": current_field.capitalize(),
        }, 409


@app.route(
    "/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"]
)  # noqa: E501
def get_validate_move(chess_figure, current_field, dest_field):
    if chess_figure not in figures:
        return {"error": "Figure does not exist."}, 404

    piece = figures[chess_figure](current_field)

    if piece.validate_move(dest_field):
        return {
            "move": "valid",
            "figure": chess_figure,
            "error": None,
            "currentField": current_field.capitalize(),
            "destField": dest_field.capitalize()
        }, 200
    else:
        return {
            "move": "invalid",
            "figure": chess_figure,
            "error": "Current move is not permitted.",
            "currentField": current_field.capitalize(),
            "destField": dest_field.capitalize(),
        }, 409


if __name__ == "__main__":
    app.run(debug=True)
