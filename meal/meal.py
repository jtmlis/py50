#!/usr/bin/env python3
#https://cs50.harvard.edu/python/2022/psets/1/meal/
#
def main():
    userTime = str(input("Enter the time"))
    return convert(userTime)
    #return meal_time(userTime)
def convert(userTime: str):
    pm = False
    if "pm" in userTime:
        userTime = userTime.replace("pm","")
        pm = True
    userTime = userTime.replace("am", "")
    hour, minutes = userTime.split(":")
    hour = float(hour)
    minutes = float(minutes)
    minutes = minutes / 60
    if pm:
        hour += 12
    return hour + minutes
def meal_time(time: float):
    """returns what type of meal it is time for"""
    if time > 24.00 or time < 0:
        return ("hmm they are only 24 hours in a day.")
    elif time <= 24 and time >=18:
        return("It is dinner Time. ")
    elif time <= 18 and time >=12:
        return("It is dinner Time. ")
    elif time <= 12 and time >=6:
        return("breakfast time")

# if __name__ == "__main__" :
    # main()
