#!/usr/bin/env python3
# https://cs50.harvard.edu/python/2022/psets/2/camel/
#

# Takes user Str in camelCase
# Converts it to  to snake_case
def main():
    userString = str(input())
    return (camelcase_converter(userString))

def camelcase_converter(userString: str):
    for char in userString:
        if char.isupper():
            print("_"+char.lower(), end="")
        else:
            print(char,sep="")

# main()
