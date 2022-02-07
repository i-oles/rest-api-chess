from app import app
import json


def test_get_available_moves_check_status_200():
    with app.test_client() as client:
        resp = client.get("/api/v1/queen/f8")
        assert resp.status_code == 200


def test_get_available_moves_check_status_409():
    with app.test_client() as client:
        resp = client.get("/api/v1/queen/g10")
        assert resp.status_code == 409


def test_get_available_moves_check_status_404():
    with app.test_client() as client:
        resp = client.get("/api/v1/quen/g1")
        assert resp.status_code == 404


def test_get_available_moves_contetnt():
    with app.test_client() as client:
        resp = client.get("/api/v1/rook/A4")
        assert resp.content_type == "application/json"


def test_get_available_moves_json_data():
    with app.test_client() as client:
        resp = client.get("/api/v1/knight/A1")
        expected = {
            "availableMoves": ["B3", "C2"],
            "error": None,
            "figure": "knight",
            "currentField": "A1",
        }

        assert json.loads(resp.get_data()) == expected


def test_get_available_moves_json_wrong_input():
    with app.test_client() as client:
        resp = client.get("/api/v1/bishop/f15")
        expected = {
            "availableMoves": [],
            "error": "Field does not exist.",
            "figure": "bishop",
            "currentField": "F15",
        }

        assert json.loads(resp.get_data()) == expected


def get_validate_move_check_status_200():
    with app.test_client() as client:
        resp = client.get("/api/v1/knight/c1/d3")
        assert resp.status_code == 200


def get_validate_move_check_status_409():
    with app.test_client() as client:
        resp = client.get("/api/v1/knight/a1/e8")
        assert resp.status_code == 409


def get_validate_move_check_status_404():
    with app.test_client() as client:
        resp = client.get("/api/v1/knight/c2/dd")
        assert resp.status_code == 404


def test_get_validate_move_contetnt():
    with app.test_client() as client:
        resp = client.get("/api/v1/pawn/A4")
        assert resp.content_type == "application/json"


def test_get_validate_move_json_data():
    with app.test_client() as client:
        resp = client.get("/api/v1/king/a2/a3")
        expected = {
            "move": "valid",
            "figure": "king",
            "error": None,
            "currentField": "A2",
            "destField": "A3",
        }

        assert json.loads(resp.get_data()) == expected


def test_get_validate_move_json_wrong_input():
    with app.test_client() as client:
        resp = client.get("/api/v1/knight/C4/V8")

        expected = {
            "move": "invalid",
            "figure": "knight",
            "error": "Current move is not permitted.",
            "currentField": "C4",
            "destField": "V8",
        }

        assert json.loads(resp.get_data()) == expected
