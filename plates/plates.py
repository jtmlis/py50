def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    n = [0,1,2,3,4,5,6,7,8,9]
    """for char in string 0-3 return valid"""
    part1 = s[0:2]
    part2 = s[3:]
    for c in part1:
        if c not in n:
            return True
        else:
            return False
    for c in part2:
        if c in n:
           return True
        else:
           return False

#main()
