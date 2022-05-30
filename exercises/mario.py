# Define the amount of squares "3"
def main():
    print_sqaure(3)

# Prints each row of squares


def print_sqaure(size):

    for i in range(size):
        print_row(size)

# Taking the size from the main function "3", and then * it by itself, and printing it.


def print_row(width):
    print("#" * width)


'''
    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")
        # Prints the brick in each row in a new line
        print()
'''

main()
