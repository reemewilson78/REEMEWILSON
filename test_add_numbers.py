"""Unit tests for add_numbers module."""

import pytest
from add_numbers import add


def test_add_positive_integers():
    assert add(2, 3) == 5


def test_add_negative_integers():
    assert add(-2, -3) == -5


def test_add_positive_and_negative():
    assert add(5, -3) == 2


def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0


def test_add_floats():
    assert pytest.approx(add(2.5, 3.1)) == 5.6
    assert pytest.approx(add(-1.5, 2.5)) == 1.0
