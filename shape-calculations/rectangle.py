#This program provides functions that allow you to find the area and perimeter of a rectangle.

#programmed by Hethur Aluma | 2/19/20

import math

def calc_rect_area():
    """Calculates the area of a rectangle."""
    length = float(input("What is the length of your rectangle? "))
    width = float(input("What is the width of your rectangle? "))
    rect_area = length * width
    print("The area of the rectangle is:", rect_area)

def calc_rect_perim():
    """Calculates the perimeter of a rectsangle."""
    length = float(input("What is the length of your rectangle? "))
    width = float(input("What is the width of your rectangle? "))
    rect_perim = length + length + width + width
    print("The area of the rectangle is:", rect_perim)
