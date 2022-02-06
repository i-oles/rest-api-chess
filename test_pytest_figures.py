import pytest
from figures import Figure, Pawn, Knight, Bishop, Rook, Queen, King
# from unittest.mock import patch

"""
class FigureTest(TestCase):
    @patch("figures.Figure.__abstractmethods__", set())
    def test_create_figure(self):
        figure = Figure("H2")
        self.assertEqual(figure.current_field, "H2")

    def test_list_available_moves(self):
        pass

    def test_validate_move(self):
        pass
"""

def test_pawn_create():
    pawn = Pawn("H5")
    assert pawn.current_field == "H5"

def test_list_available_moves():
    pawn = Pawn("A5")
    assert pawn.list_available_moves() == ["A6"]

    pawn = Pawn("A1")
    assert pawn.list_available_moves() == ["A2"]

    pawn = Pawn("a2")
    assert pawn.list_available_moves() == ["A3", "A4"]

    pawn = Pawn("b7")
    assert pawn.list_available_moves() == ["B8"]

    pawn = Pawn("bb")
    assert pawn.list_available_moves() == []

def test_validate_move():
    pawn = Pawn("h6")
    assert pawn.validate_move("h7") is True

    pawn = Pawn("g6")
    assert pawn.validate_move("h9") is False

    pawn = Pawn("bb")
    assert pawn.validate_move("h8") is False

"""
class KnightTest(TestCase):
    def test_knight_create(self):
        knight = Knight("C5")
        self.assertEqual(knight.current_field, "C5")

    def test_list_available_moves(self):
        knight = Knight("D2")
        expected = sorted(["B1", "B3", "C4", "E4", "F3", "F1"])
        self.assertListEqual(sorted(knight.list_available_moves()), expected)

        knight = Knight("a5")
        expected = sorted(["B7", "C6", "C4", "B3"])
        self.assertListEqual(sorted(knight.list_available_moves()), expected)

        knight = Knight("hh")
        self.assertListEqual(knight.list_available_moves(), [])

    def test_validate_move(self):
        knight = Knight("d7")
        self.assertTrue(knight.validate_move("f8"))

        knight = Knight("g6")
        self.assertFalse(knight.validate_move("h9"))

        knight = Knight("bb")
        self.assertFalse(knight.validate_move("h8"))


class BishopTest(TestCase):
    def test_bishop_create(self):
        bishop = Bishop("e3")
        self.assertEqual(bishop.current_field, "e3")

    def test_list_available_moves(self):
        bishop = Bishop("g2")
        expected = sorted(["A8", "B7", "C6", "D5", "E4", "H3", "F3", "H1", "F1"])

        self.assertListEqual(sorted(bishop.list_available_moves()), expected)

        bishop = Bishop("G2")
        expected = sorted(["A8", "B7", "C6", "D5", "E4", "H3", "F3", "H1", "F1"])

        self.assertListEqual(sorted(bishop.list_available_moves()), expected)

        bishop = Bishop("a1")
        expected = sorted(["B2", "C3", "D4", "E5", "F6", "G7", "H8"])
        self.assertListEqual(sorted(bishop.list_available_moves()), expected)

        bishop = Bishop("ee")
        self.assertListEqual(bishop.list_available_moves(), [])

    def test_validate_move(self):
        bishop = Bishop("h7")
        self.assertTrue(bishop.validate_move("e4"))

        bishop = Bishop("E1")
        self.assertTrue(bishop.validate_move("c3"))

        bishop = Bishop("G7")
        self.assertFalse(bishop.validate_move("G10"))

        bishop = Bishop("f")
        self.assertFalse(bishop.validate_move("a5"))


class RookTest(TestCase):
    def test_rook_create(self):
        rook = Rook("f2")
        self.assertEqual(rook.current_field, "f2")

    def test_list_available_moves(self):
        rook = Rook("f4")
        expected = sorted(
            [
                "F1",
                "F2",
                "F3",
                "F5",
                "F6",
                "F7",
                "F8",
                "A4",
                "B4",
                "C4",
                "D4",
                "E4",
                "G4",
                "H4",
            ]
        )
        self.assertListEqual(sorted(rook.list_available_moves()), expected)

        rook = Rook("F4")
        expected = sorted(
            [
                "F1",
                "F2",
                "F3",
                "F5",
                "F6",
                "F7",
                "F8",
                "A4",
                "B4",
                "C4",
                "D4",
                "E4",
                "G4",
                "H4",
            ]
        )
        self.assertListEqual(sorted(rook.list_available_moves()), expected)

        rook = Rook("h1")
        expected = sorted(
            [
                "H8",
                "H7",
                "H6",
                "H5",
                "H4",
                "H3",
                "H2",
                "G1",
                "F1",
                "E1",
                "D1",
                "C1",
                "B1",
                "A1",
            ]
        )
        self.assertListEqual(sorted(rook.list_available_moves()), expected)

        rook = Rook("")
        self.assertListEqual(rook.list_available_moves(), [])

    def test_validate_move(self):
        rook = Rook("e4")
        self.assertTrue(rook.validate_move("b4"))

        rook = Rook("D4")
        self.assertTrue(rook.validate_move("C4"))

        rook = Rook("f2")
        self.assertFalse(rook.validate_move("G8"))

        rook = Rook("..")
        self.assertFalse(rook.validate_move(";;"))


class QueenTest(TestCase):
    def test_queen_create(self):
        queen = Queen("g1")
        self.assertEqual(queen.current_field, "g1")

        queen = Queen("H1")
        self.assertEqual(queen.current_field, "H1")

    def test_list_available_moves(self):
        queen = Queen("D4")
        expected = sorted(
            [
                "H8",
                "D8",
                "G7",
                "D7",
                "A7",
                "F6",
                "D6",
                "B6",
                "E5",
                "D5",
                "C5",
                "H4",
                "G4",
                "F4",
                "E4",
                "C4",
                "B4",
                "A4",
                "E3",
                "D3",
                "C3",
                "F2",
                "D2",
                "B2",
                "G1",
                "D1",
                "A1",
            ]
        )
        self.assertListEqual(sorted(queen.list_available_moves()), expected)

        queen = Queen("a8")
        expected = sorted(
            [
                "H8",
                "G8",
                "F8",
                "E8",
                "D8",
                "C8",
                "B8",
                "B7",
                "A7",
                "C6",
                "A6",
                "D5",
                "A5",
                "E4",
                "A4",
                "F3",
                "A3",
                "G2",
                "A2",
                "H1",
                "A1",
            ]
        )
        self.assertListEqual(sorted(queen.list_available_moves()), expected)

        queen = Queen("9")
        self.assertListEqual(queen.list_available_moves(), [])

    def test_validate_move(self):
        queen = Queen("e1")
        self.assertTrue(queen.validate_move("a5"))

        queen = Queen("E3")
        self.assertTrue(queen.validate_move("H6"))

        queen = Queen("h1")
        self.assertFalse(queen.validate_move("f5"))

        queen = Queen("8")
        self.assertFalse(queen.validate_move("a4"))


class KingTest(TestCase):
    def test_king_create(self):
        king = King("c7")
        self.assertEqual(king.current_field, "c7")

        king = King("c7")
        self.assertNotEqual(king.current_field, "C7")

    def test_list_available_moves(self):
        king = King("b2")
        expected = sorted(["A1", "A2", "A3", "B3", "B1", "C1", "C2", "C3"])
        self.assertListEqual(sorted(king.list_available_moves()), expected)

        king = King("H1")
        expected = sorted(["G1", "G2", "H2"])
        self.assertListEqual(sorted(king.list_available_moves()), expected)

        king = King("d55")
        self.assertListEqual(king.list_available_moves(), [])

    def test_validate_move(self):
        king = King("a4")
        self.assertTrue(king.validate_move("b3"))

        king = King("E7")
        self.assertTrue(king.validate_move("D8"))

        king = King("c8")
        self.assertFalse(king.validate_move("a1"))

        king = King("a10")
        self.assertFalse(king.validate_move("a11"))

"""