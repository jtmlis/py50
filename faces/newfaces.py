#promts user for input
def convert(uString):
    uString = uString.replace(":(", "😐")
    uString = uString.replace(":)", "🙂")
    print (uString)
def main():
    uString = str(input())
    convert(uString)
main()
