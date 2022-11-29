#https://cs50.harvard.edu/python/2022/psets/3/fuel/

from fuel import fuelgauge
# Tests from website

# "3/4" should output 75 %
def test_fuelgauge():
    assert fuelgauge("3/4") == ("75%")
# 1/4 outputs 25%
# 4/4 outputs F
# 0/4 outputs E
# 4/0 outputs ZeroDivisonError
# three/four ouputs ValueError
# 5/4 outputs prompt for user again
