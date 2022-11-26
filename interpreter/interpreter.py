# import ipdb;

#!/usr/bin/env python3
# https://cs50.harvard.edu/python/2022/psets/1/interpreter/
def main():
    # ipdb.set_trace()
    userInput = str(input(Enter the formula:")
    isValid(userInput
    x,operator,y = userInput.split(" ")
    print (formulaConversion(userInput))


def formulaConversion(userInput):

    x = int(x)
    y = str(y)
    z = int(z)
    # print("x is",x)

    # print("y is",y)
    # print("z is",z)
    if y  == "/":
        return (x / z)
    elif y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
main()

#take user input

#TODO write test for user input(is it 0-9)
#determine mathematical operator
#apply operator
