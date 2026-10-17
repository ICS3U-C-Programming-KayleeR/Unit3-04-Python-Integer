#!/usr/bin/env python3
# Created By: Kaylee Ralejoe
# Date: 17,10,2026
# The program has the user input
# an integer. Depending on what integer the user inputs,
# the program will say what type of integer it is
# by comparing it to some conditions.


def main():
    # get the user's input of an integer
    user_int = int(input("Input any integer: "))

    # check what type of integer the user input
    if user_int > 0:
        print("That is a positive integer")

    elif user_int < 0:
        print("That is a negative integer")

    else:
        print("The integer is 0")


if __name__ == "__main__":
    main()
