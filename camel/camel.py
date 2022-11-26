#!/usr/bin/env python3
# https://cs50.harvard.edu/python/2022/psets/2/camel/
#
# import ipdb
# Takes user Str in camelCase
# Converts it to  to snake_case
def main():
    # ipdb.set_trace()
    userString = str(input())
    return camelcase_converter(userString)

def camelcase_converter(userString: str):
    snake_case = ""
    for char in userString:
        if char.isupper():
            snake_case += ("_"+char.lower())
        else:
            snake_case += (char)
    return snake_case.strip(" ")
# main()
