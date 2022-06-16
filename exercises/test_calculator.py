from calculator import square

# Common to call the function that is being tested, with test_(function)

# Assert will show you the traceback information i.e. the lines of code that the error.

# Installed pytest which can sort of "automate" and can be used as a testing library.

'''
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")


def main():
    test_square()


if __name__ == "__main__":
    main()
'''


# Running py test on this code, automates the testing process. (pytest test_calculator.py in terminal)


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0
