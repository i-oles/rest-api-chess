from figures import Pawn, Knight, Bishop, Rook, Queen, King
from werkzeug.exceptions import HTTPException
import json

from flask import Flask

"""
bugs:
1. pawn promotion -> ex. 4 x D8
2. pawn: a8 -> return error 'null'(my implementation),
    or 'error: field does not exist' (chess lib implementation)
3. pawn: a1 --> zwraca a2, a3
4. pawn on a1 never stands - ?
5. testing abstract method
X6. abstract method implementation
7. status codes check, 500
8. status 404 -> whole dict of just one line error
9. test for 500 status

questions:
7. test 'create_king' c7 -> C7
8. second GET - 'field does not exist'
9. 'move': 'valid' hardcoded/returned
10. 'validate_moves' can return bool
11. validate dest_field?
12. comments?

1. flake8 - line 68 too long
2. pip freeze -> too many imports?
3. could not import modules in tests folder, tests outside
4. in readme only valid cases?


todo:
1. security
2. validate response status codes
3. type hints
4. flake8 validations

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
def get_available_moves(chess_figure: str, current_field: str):
    if chess_figure not in figures:
        return {"error": f"Chess figure: {chess_figure} does not exist."}, 404

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
def get_validate_move(chess_figure: str, current_field: str, dest_field: str):

    if chess_figure not in figures:
        return {"error": f"Chess figure: {chess_figure} does not exist."}, 404

    piece = figures[chess_figure](current_field)

    if piece.validate_move(dest_field):
        return {
            "move": "valid",
            "figure": chess_figure,
            "error": None,
            "currentField": current_field.capitalize(),
            "destField": dest_field.capitalize(),
        }, 200
    else:
        return {
            "move": "invalid",
            "figure": chess_figure,
            "error": "Current move is not permitted.",
            "currentField": current_field.capitalize(),
            "destField": dest_field.capitalize(),
        }, 409


# https://sites.uclouvain.be/P2SINF/flask/errorhandling.html
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


@app.errorhandler(500)
def server_error(e):
    logging.exception(f"An error occurred during a request: {e}.")
    return Response(
        response="An internal error occurred. See logs for full stacktrace.",
        status=500,
    )


if __name__ == "__main__":
    app.run(debug=True)
