from figures import Figure, Pawn, Knight, Bishop, Rook, Queen, King
from abc import ABCMeta


def test_abstract_figure():
    Figure.__abstractmethods__ = set()

    class ABCTest(Figure):
        def __init__(self, current_field: str):
            self.current_field = current_field

    knight = ABCTest("a1")
    assert isinstance(Figure, ABCMeta)
    assert knight.list_available_moves() is None
    assert knight.validate_move("b3") is None


def test_pawn_create():
    pawn = Pawn("H5")
    assert pawn.current_field == "H5"


def test_pawn_list_available_moves_1():
    pawn = Pawn("A5")
    assert pawn.list_available_moves() == ["A6"]


def test_pawn_list_available_moves_2():
    pawn = Pawn("A1")
    assert pawn.list_available_moves() == ["A2"]


def test_pawn_list_available_moves_3():
    pawn = Pawn("a2")
    assert pawn.list_available_moves() == ["A3", "A4"]


def test_pawn_list_available_moves_4():
    pawn = Pawn("b7")
    assert pawn.list_available_moves() == ["B8"]


def test_pawn_list_available_moves_5():
    pawn = Pawn("bb")
    assert pawn.list_available_moves() == []


def test_pawn_validate_move_1():
    pawn = Pawn("h6")
    assert pawn.validate_move("h7") is True


def test_pawn_validate_move_2():
    pawn = Pawn("g6")
    assert pawn.validate_move("h9") is False


def test_pawn_validate_move_3():
    pawn = Pawn("bb")
    assert pawn.validate_move("h8") is False


def test_knight_create():
    knight = Knight("C5")
    assert knight.current_field == "C5"


def test_knight_list_available_moves_1():
    knight = Knight("D2")
    expected = sorted(["B1", "B3", "C4", "E4", "F3", "F1"])
    assert sorted(knight.list_available_moves()) == expected


def test_knight_list_available_moves_2():
    knight = Knight("a5")
    expected = sorted(["B7", "C6", "C4", "B3"])
    assert sorted(knight.list_available_moves()) == expected


def test_knight_list_available_moves_3():
    knight = Knight("hh")
    assert sorted(knight.list_available_moves()) == []


def test_knight_validate_move_1():
    knight = Knight("d7")
    assert knight.validate_move("f8") is True


def test_knight_validate_move_2():
    knight = Knight("g6")
    assert knight.validate_move("h9") is False


def test_knight_validate_move_3():
    knight = Knight("bb")
    assert knight.validate_move("h8") is False


def test_bishop_create():
    bishop = Bishop("e3")
    assert bishop.current_field == "e3"


def test_bishop_list_available_moves_1():
    bishop = Bishop("g2")
    expected = sorted(["A8", "B7", "C6", "D5", "E4", "H3", "F3", "H1", "F1"])
    assert sorted(bishop.list_available_moves()) == expected


def test_bishop_list_available_moves_2():
    bishop = Bishop("G2")
    expected = sorted(["A8", "B7", "C6", "D5", "E4", "H3", "F3", "H1", "F1"])
    assert sorted(bishop.list_available_moves()) == expected


def test_bishop_list_available_moves_3():
    bishop = Bishop("a1")
    expected = sorted(["B2", "C3", "D4", "E5", "F6", "G7", "H8"])
    assert sorted(bishop.list_available_moves()) == expected


def test_bishop_list_available_moves_4():
    bishop = Bishop("ee")
    assert sorted(bishop.list_available_moves()) == []


def test_bishop_validate_move_1():
    bishop = Bishop("h7")
    assert bishop.validate_move("e4") is True


def test_bishop_validate_move_2():
    bishop = Bishop("E1")
    assert bishop.validate_move("c3") is True


def test_bishop_validate_move_3():
    bishop = Bishop("G7")
    assert bishop.validate_move("G10") is False


def test_bishop_validate_move_4():
    bishop = Bishop("f")
    assert bishop.validate_move("a5") is False


def test_rook_create():
    rook = Rook("f2")
    assert rook.current_field == "f2"


def test_rook_list_available_moves_1():
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
    assert sorted(rook.list_available_moves()) == expected


def test_rook_list_available_moves_2():
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
    assert sorted(rook.list_available_moves()) == expected


def test_rook_list_available_moves_3():
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
    assert sorted(rook.list_available_moves()) == expected


def test_rook_list_available_moves_4():
    rook = Rook("")
    assert rook.list_available_moves() == []


def test_rook_validate_move_1():
    rook = Rook("e4")
    assert rook.validate_move("b4") is True


def test_rook_validate_move_2():
    rook = Rook("D4")
    assert rook.validate_move("C4") is True


def test_rook_validate_move_3():
    rook = Rook("f2")
    assert rook.validate_move("G8") is False


def test_rook_validate_move_4():
    rook = Rook("..")
    assert rook.validate_move(";;") is False


def test_queen_create_1():
    queen = Queen("g1")
    assert queen.current_field == "g1"


def test_queen_create_2():
    queen = Queen("H1")
    assert queen.current_field == "H1"


def test_queen_list_available_moves_1():
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
    assert sorted(queen.list_available_moves()) == expected


def test_queen_list_available_moves_2():
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
    assert sorted(queen.list_available_moves()) == expected


def test_queen_list_available_moves_3():
    queen = Queen("9")
    assert queen.list_available_moves() == []


def test_queen_validate_move_1():
    queen = Queen("e1")
    assert queen.validate_move("a5") is True


def test_queen_validate_move_2():
    queen = Queen("E3")
    assert queen.validate_move("H6") is True


def test_queen_validate_move_3():
    queen = Queen("h1")
    assert queen.validate_move("f5") is False


def test_queen_validate_move_4():
    queen = Queen("8")
    assert queen.validate_move("a4") is False


def test_king_create_1():
    king = King("c7")
    assert king.current_field == "c7"


def test_king_create_2():
    king = King("c7")
    assert king.current_field != "C7"


def test_king_list_available_moves_1():
    king = King("b2")
    expected = sorted(["A1", "A2", "A3", "B3", "B1", "C1", "C2", "C3"])
    assert sorted(king.list_available_moves()) == expected


def test_king_list_available_moves_2():
    king = King("H1")
    expected = sorted(["G1", "G2", "H2"])
    assert sorted(king.list_available_moves()) == expected


def test_king_list_available_moves_3():
    king = King("d55")
    assert king.list_available_moves() == []


def test_king_validate_move_1():
    king = King("a4")
    assert king.validate_move("b3") is True


def test_king_validate_move_2():
    king = King("E7")
    assert king.validate_move("D8") is True


def test_king_validate_move_3():
    king = King("c8")
    assert king.validate_move("a1") is False


def test_king_validate_move_4():
    king = King("a10")
    assert king.validate_move("a11") is False
