#!/usr/bin/env python3
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    """accepts a str as input
    format as $##.##, where each # is a decimal digit
    remove the trailing % and return the string as a float so if 50 return 50.00"""

def percent_to_float(p):
    # TODO
    """accepts a percent as input
    remove the trailing % and return the percetage as a float so if 15% return 0.15"""

main()
