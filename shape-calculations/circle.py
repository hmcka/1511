#This program provides functions that allow you to find the area and circumference of a circle.

#programmed by Hethur Aluma | 2/19/20

import math

def calc_circle_area():
    """Calculates the area of a circle"""
    radius = float(input("What is the radius of your circle? "))
    circle_area = math.pi * radius
    print("The area of the circle is:", circle_area)

def calc_circle_circum():
    """Calculates the circumference of a circle."""
    radius = float(input("What is the radius of your circle? "))
    circle_circum = 2 * math.pi * radius
    print("The circumference of the circle is:", circle_circum)
