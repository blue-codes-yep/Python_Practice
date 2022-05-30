# Counting with a while loop to print.
'''
i = 0
while i < 3:
    print("meow")
    i += 1 
'''
# Using _ if it's something that is not so important but just required to run, and not being used later.

'''
for _ in range(3):
    print("meow")
'''
# \n creates an extra line whenever ending, so ending it with an empty string will cause the last line to be an empty string.

# print("meow\n" * 3, end="")


# Writing functions to take a input, and print out a string depending on the number of times the user inputs.

'''
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n "))
        if n > 0:
            break
        return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
'''
