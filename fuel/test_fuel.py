#https://cs50.harvard.edu/python/2022/psets/3/fuel/

from fuel import fuel_gauge
# Tests from website

# "3/4" should output 75 %
def test_fuel_gauge():
    assert fuel_gauge("3/4") == ("75%")
# 1/4 outputs 25%
    assert fuel_gauge("1/4") == ("25%")
# 4/4 outputs F
    assert fuel_gauge("4/4") == ("F")
# 0/4 outputs E
    assert fuel_gauge("0/100") == ("E")
# 4/0 outputs ZeroDivisionError
# three/four outputs ValueError
# 5/4 outputs prompt for user again
