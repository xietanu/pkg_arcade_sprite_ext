"""Tests for Coords"""
from src.arcade_sprite_ext import coords


def test_coords_addition_type():
    """Test addition returns Coords"""
    coords_1 = coords.Coords(0, 0)
    coords_2 = coords.Coords(0, 0)

    assert isinstance(coords_1 + coords_2, coords.Coords)


def test_coords_addition_basic():
    """Basic addition test"""
    coords_1 = coords.Coords(2, 1)
    coords_2 = coords.Coords(5, 4)

    expected = coords.Coords(7, 5)

    assert coords_1 + coords_2 == expected


def test_coords_addition_negative():
    """Negative addition test"""
    coords_1 = coords.Coords(2, 1)
    coords_2 = coords.Coords(-7, -2)

    expected = coords.Coords(-5, -1)

    assert coords_1 + coords_2 == expected


def test_coords_subtraction_type():
    """Test addition returns Coords"""
    coords_1 = coords.Coords(0, 0)
    coords_2 = coords.Coords(0, 0)

    assert isinstance(coords_1 - coords_2, coords.Coords)


def test_coords_subtraction_basic():
    """Basic subtraction test"""
    coords_1 = coords.Coords(7, 1)
    coords_2 = coords.Coords(5, 4)

    expected = coords.Coords(2, -3)

    assert coords_1 - coords_2 == expected
