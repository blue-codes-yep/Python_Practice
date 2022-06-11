import sys

if len(sys.argv) < 2:
    print("Too few arguments")

for arg in sys.argv[1:-1]:
    print("Hello my name is", arg)

# The first argument in argv, is the name of the program.

# Argv[1] takes the user's argument and prints it out.
