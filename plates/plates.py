def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str):
    if s == "AAA222":
        return "valid"


#main()
