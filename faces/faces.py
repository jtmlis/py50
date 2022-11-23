# file with logging capapbilities to be further studied later
# more help at https://github.com/spiside/pdb-tutorial
import ipdb
import logging
#promts user for input
def convert(uString):
    uString = uString.replace(":(", "😐")
    uString = uString.replace(":)", "🙂")

def main():
    uString = str(input())
    ipdb.set_trace()
    convert(uString)
    print(uString)
    # this is what glenn was referenicing when speaking of not using print?
    logging.error(f'{uString} raised an error')
if __name__ == '__main__':
     main()
