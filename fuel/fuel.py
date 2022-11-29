#https://cs50.harvard.edu/python/2022/psets/3/fuel/
import ipdb
# Takes x & y as INT


def main():
    ipdb.set_trace()
    gastank = input("Fraction :")
    return fuel_gauge(gastank)


def fuel_gauge(fuel):
    x,y, = fuel.split("/")
    status = (int(x) / int(y) * 100)
    status = int(status)
    return f"{status}%"














# returns as a rounded % to nearest Int
# If less than 1% return Empty
# If greater than 99% return Full


# if x or y not an INT prompt again
# is X greater than Y
# if y is 0
#main()