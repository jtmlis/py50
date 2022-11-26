#!/usr/bin/env python3
#https://cs50.harvard.edu/python/2022/psets/1/meal/
#
def main():
    userTime = str(input("Enter the time"))
    return convert(userTime)
def convert(userTime: str):
    userTime = userTime.replace("am", "")
    hour, minutes = userTime.split(":")
    hour = float(hour)
    minutes = float(minutes)
    minutes = minutes / 60
    return hour + minutes
# if __name__ == "__main__" :
    # main()
