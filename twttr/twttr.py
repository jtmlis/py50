#!/usr/bin/env python3
# https://cs50.harvard.edu/python/2022/psets/2/twttr
# answer from https://www.youtube.com/watch?v=Xc3eaIU9XGw
# have to redo on my own I went wrong trying to use a dictionary
answer = str(input("input: "))
print("output: ", end="")

for letter in answer:
    if not letter.lower() in ["a","e","o","u","i"]:
        print(letter,end="")
print()
