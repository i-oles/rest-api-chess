from pawn import Pawn
from figure import Figure
import json

from flask import Flask
import chess

app = Flask(__name__)


def field_exist(current_field):
    try:
        chess.parse_square(current_field)
    except ValueError:
        return False
   

def available_moves_template(available_moves, figure, current_field, error='null'):
    return {'availableMoves': available_moves,
    "error": error,
    "figure": figure,
    "currentField": current_field}


@app.route("/api/v1/<chess_figure>/<current_field>", methods=['GET'])
def get_available_moves(chess_figure, current_field):
    if chess_figure == 'pawn':
        p = Pawn(current_field)
        if field_exist(current_field) == False:
            error = 'Field does not exist'
            return available_moves_template( [], chess_figure, current_field.capitalize(), error )
        else:
            available_moves = p.list_available_moves()
            return available_moves_template(available_moves, chess_figure, current_field.capitalize())


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=['GET'])
def validate_move(chess_figure, current_field, dest_field):
    pass



if __name__ == '__main__':
    app.run(debug=True)

