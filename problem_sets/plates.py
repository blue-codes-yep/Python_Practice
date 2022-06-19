import string
import re

# Makes sure the first two characters of the string aren't digits.
plate_pattern = re.compile('\D*\d*')


def main():
    plate = input("Plate: ")
    tests = [exclusions, platecheck, checkzero]
    invalid = any(test(plate) for test in tests)
    if invalid:
        print("Invalid")
    else:
        print("Valid")


def exclusions(s):
    if any(c in string.punctuation for c in s):
        return True
    return len(s) > 6 or len(s) < 2


def platecheck(s):
    return not plate_pattern.fullmatch(s)


def checkzero(s):
    p = re.compile(r"^[^\d]*0.*\d?")
    matched = re.search(p, s)
    return re.search(p, s) != None


if __name__ == "__main__":
    main()
