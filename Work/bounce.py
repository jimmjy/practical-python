"""
    A rubber ball is dropped from a height of 100 meters and each time it hits the gorund,
    it bonces back up to 3/5 the height it fell.
    
    Write a program that prints a table showing the height of the first 10 bounces.
"""

# bounce.py
#
# Exercise 1.5
drop_height = 100
bounce_factor = 3 / 5

for i in range(10):
    drop_height *= bounce_factor
    print(round(drop_height, 4))