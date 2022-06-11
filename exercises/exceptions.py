def main():
    x = get_int("What's x")
    print(f"x is {x}")  # f is used to format x, into the print string.


def get_int(prompt):
    while True:
        try:
            x = (int(input(prompt)))
        except ValueError:
            # Can also just pass the ValueError to repeat till you get an int.
            print("x is not an integer")
        else:
            return x

# Returning a value will also break you out of a loop


main()
