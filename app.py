from figures import Pawn, Knight, Bishop, Rook, Queen, King
from werkzeug.exceptions import HTTPException

from flask import Flask


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
    available_moves = piece.list_available_moves()

    if available_moves is not None:
        return {
            "availableMoves": available_moves,
            "error": None,
            "figure": chess_figure,
            "currentField": current_field.capitalize(),
        }, 200
    else:
        return {
            "availableMoves": [],
            "error": "Field does not exist.",
            "figure": chess_figure,
            "currentField": current_field.capitalize(),
        }, 409


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
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


@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, HTTPException):
        return {"error": e.name}, e.code
    else:
        return {"error": "Server error"}, 500


if __name__ == "__main__":
    app.run()
