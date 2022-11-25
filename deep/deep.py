#!/usr/bin/env python3
def main():
    userInput = str(input("What is the question of life?").lower().strip(" "))
    return validate(userInput)
def validate(userInput):
    match(userInput):
        case "42" | "forty-two" | "forty two" | "fortytwo" :
            print("Yes")
        case _:
            print("No")


main()
