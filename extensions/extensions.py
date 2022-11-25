#!/usr/bin/env python3
# https://cs50.harvard.edu/python/2022/psets/1/extensions/
# Return Mime format for file extensions
""".gif
.jpg
.jpeg
.png
.pdf
.txt
.zip"""

def main():
    """takes the user input """
    extension = str (input("Enter your file name : ").lower().lstrip(" ").rstrip(" "))
    return validate(extension)

def validate(x: str):
    """if validate is in the variables return positive"""
    if  x.endswith(".jpeg") or x.endswith(".jpg"):
            print("image/jpeg")
    elif  x.endswith(".gif"):
        print("image/gif")
    elif x.endswith(".png"):
            print("image/png")
    elif x.endswith(".pdf"):
            print("application/pdf")
    elif x.endswith(".txt"):
            print("text/plain")
    elif x.endswith(".zip"):
            print("application/zip")
    else:
        print("application/octet-stream")
main()
