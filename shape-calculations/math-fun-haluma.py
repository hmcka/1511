#This program allows you to find the area and circumference of a circle and a rectangle.

#programmed by Hethur Aluma | 2/18/20

from circle import calc_circle_area
from circle import calc_circle_circum
from rectangle import calc_rect_area
from rectangle import calc_rect_perim


choice = ""

while choice != "5":
    print (
    """
    \t\tMENU

    1 - Area of a circle
    2 - Circumference of a circle
    3 - Area of a rectangle
    4 - Perimeter of a rectangle
    5 - Quit
    """
    )
    
    choice = input("Enter your choice: ")
    print()

    #find a circle area
    if choice == "1":
        calc_circle_area()

    #find the circumference of a circle
    elif choice == "2":
        calc_circle_circum()

    #find the area of a rectangle
    elif choice == "3":
        calc_rect_area()

    #find the perimenter of a rectangle
    elif choice == "4":
        calc_rect_perim()
        
    #quit
    elif choice == "5":
        print("Exiting the program")

    #some unknown choice
    else:
        print("Sorry, but ", choice, "isn't a valid choice.") 

input("Hit enter to exit.")
