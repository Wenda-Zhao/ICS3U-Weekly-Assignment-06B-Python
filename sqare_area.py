#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Jan 2021
# This program for WA06B


def calculate_area(length, width, area):
    # This function is for calcuate

    # process
    try:
        length_int = int(length)
        if length_int > 0:
            try:
                width_int = int(width)
                if width_int > 0:
                    area = length_int * width_int
                else:
                    print("width is not a positive number")
            except Exception:
                print("width is not a integer")
        else:
            print("length is not a positive number")
    except Exception:
        print("length is not a integer")

    return area


def main():
    # This function is get input

    area = -1

    # input
    length = input("Enter the length(mm):")
    width = input("Enter the width(mm)")

    # call function
    final_area = calculate_area(length, width, area)

    # output
    print("the area is {0}mm²".format(final_area))


if __name__ == "__main__":
    main()
