#!/usr/bin/env python3
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """accepts a str as input
    format as $##.##, where each # is a decimal digit
    remove the trailing % and return the string as a float so if 50 return 50.00"""
    dNoDollarSign = d.replace("$", "")
    return float(dNoDollarSign)

def percent_to_float(p):
    p_without_percent = p.replace("%","")
    p_converted = float(p_without_percent/100)
    return p_converted
main()
