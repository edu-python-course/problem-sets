from chess import func


def test_within_board():
    assert func.within_board((0, 0)) is True
    assert func.within_board((1, 1)) is True
    assert func.within_board((2, 2)) is True
    assert func.within_board((3, 3)) is True
    assert func.within_board((4, 4)) is True
    assert func.within_board((5, 5)) is True
    assert func.within_board((6, 6)) is True
    assert func.within_board((7, 7)) is True


def test_within_board_negative():
    assert func.within_board((-100, -20)) is False
    assert func.within_board((5, -5)) is False
    assert func.within_board((-5, 5)) is False
    assert func.within_board((5, 50)) is False
    assert func.within_board((8, 7)) is False
