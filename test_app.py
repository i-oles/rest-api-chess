from unittest import TestCase
from app import app


class AppTest(TestCase):
    def get_available_moves(self):
        app.testing = True
        with app.test_client() as client:
            resp = client.get("/api/v1/knight/a1")

            self.assertEqual(resp.status_code, 200)

            expected = {
                "availableMoves": ["B3", "C2"],
                "error": "null",
                "figure": "knight",
                "currentField": "A1",
            }

            self.assertEqual(json.loads(resp.get_data()), expected)

        with app.test_client() as client:
            resp = client.get("/api/v1/knight/a10")

            self.assertEqual(resp.status_code, 200)

            expected = {
                "availableMoves": [],
                "error": "Field does not exist.",
                "figure": "knight",
                "currentField": "A10",
            }

            self.assertEqual(json.loads(resp.get_data()), expected)

    def get_validate_move(self):
        app.testing = True
        with app.test_client() as client:
            resp = client.get("/api/v1/knight/c1/d3")

            self.assertEqual(resp.status_code, 200)

            expected = {
                "move": "valid",
                "figure": "knight",
                "error": "null",
                "currentField": "C1",
                "destField": "D3",
            }

            self.assertEqual(json.loads(resp.get_data()), expected)

        with app.test_client() as client:
            resp = client.get("/api/v1/knight/c1/v4")

            self.assertEqual(resp.status_code, 200)

            expected = {
                "move": "invalid",
                "figure": "knight",
                "error": "Current move is not permitted.",
                "currentField": "C1",
                "destField": "V4",
            }

            self.assertEqual(json.loads(resp.get_data()), expected)
