#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about for loop


def main():
    # This function is about for loop
    loop_number = 0
    answer_number = 0

    # input
    user_string = input("Please enter a positive integer: ")
    print("")

    # process
    try:
        user_number = int(user_string)
        if user_number >= 0:
            for loop_number in range(user_number + 1):
                answer_number = loop_number ** 2
                # output
                print("{0}² = {1}.".format(loop_number, answer_number))
        else:
            print("You didn't enter a positive integer.")
    except Exception:
        # output
        print("You didn't enter an integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
