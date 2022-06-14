#!/usr/bin/env python3

# Created by Noah McCaskill
# Created June 2022
# This program rounds a number based on user input


def round_num(user_num, round_to):
    # rounds the users number to their desired decimal place

    round_unit = 10**round_to

    user_num[0] = int(user_num[0] * round_unit + 0.5) / round_unit


def main():
    # Takes user input, passes it to round function,
    # then outputs the rounded number

    user_num = []

    print("This program rounds a number based on user input.\n")

    # input
    num_string = input("Enter the number you want to round: ")
    decimal_string = input("Enter decimal places to round to: ")

    # process
    try:
        num = float(num_string)
        user_num.append(num)
        decimal = int(decimal_string)

        if decimal >= 0:
            round_num(user_num, decimal)
            print("\nThe rounded number is {0}.".format(user_num[0]))
        else:
            print("\nThe decimal places to round to cannot be negative.")

    except Exception:
        print("\nThat cannot be rounded. Please ensure you are entering valid numbers.")

    print("\nDone.")


if __name__ == "__main__":
    main()
