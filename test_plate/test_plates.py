from problem_sets.plates import exclusions
from problem_sets.plates import platecheck
from problem_sets.plates import checkzero

import re


def test_punctuation():
    # Testing if plate contains punctuation
    assert exclusions("ABCD") == False
    assert exclusions("ABC!D") == True
    assert exclusions("ABC.A") == True


def test_length():
    # Length within 2-6 characters
    assert exclusions("ABC123") == False

    # Length longer than 6 characters
    assert exclusions("ABC1234") == True

    # Length shorter than 2 characters
    assert exclusions("A") == True


def test_platecheck():
    # Make sure that the plates start with at-least two letters first.
    assert platecheck("0Dbc") == True
    assert platecheck("D0bc") == True

    # Plate starts with two charcters.
    assert platecheck("Dbc3") == False
    assert platecheck("Abcd") == False


def test_checkzero():
    # Check if string contains zero.
    assert checkzero("0Abc") == True
    assert checkzero("Ab0c") == True
    assert checkzero("Abcde") == False
