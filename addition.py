#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program adds 2 integers


def main():
    # this function adds the 2 numbers

    # input
    integer_1 = int(input("Enter the first number to add (integer): "))
    integer_2 = int(input("Enter the second number to add (integer): "))

    # process
    addition = integer_1 + integer_2

    # output
    print(" ")
    print("{0} + {1} = {2}".format(integer_1, integer_2, addition))
    print(" ")
    print("Done.")


if __name__ == "__main__":
    main()
