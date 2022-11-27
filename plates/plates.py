# Used annas video for help
#import ipdb


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Anna's code
def is_valid(s: str):
    # must contain 6 chars max, 2 chars min
    #ipdb.set_trace()
    if len(s) < 2 or len(s) > 6:
        return False
    # Begins with 2 letters
    if s[0] == s.isalpha() == False or s[1] == s.isalpha() == False:
        return False

    # cannot start with 0
    if s[0] == "0":
        return False
    # can not end with a letter
    if s[-1] == s.isalpha():
        return False

    # while loop
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1
        # end of loop -> put variable
    for c in s:
        if c in [".", "?", "!", " "]:
            return False
    return True


#main()
