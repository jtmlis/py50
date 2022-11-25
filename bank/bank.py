#!/usr/bin/env python3
# https://cs50.harvard.edu/python/2022/psets/1/bank/


def main():
    """takes input and runs validate"""
    greeting = str(input("Greet me:").lower().strip())
    return greetingValidator(greeting)

def greetingValidator(greeting:str):
    """takes a greeting and validates if it is up to the hello rule.
    see seinfeld episode for more details"""
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h" or "H"):
        print("$20")
    else:
        print("$100")


main()
