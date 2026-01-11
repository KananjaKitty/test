# # def rectangle(length, width):
# #     length = float(input("Enter the length of the rectangle: "))
# #     width = float(input("Enter the width of the rectangle: "))
# #     area = length * width
    
# #     print("The area of the rectangle is: " ,area )

# # def triangle(base, height):
# #     base = float(input("Enter the base of the triangle: "))
# #     height = float(input("Enter the height of the triangle: "))
# #     area = base * height
    
# #     print("The area of the triangle is:" ,area)

# # def circle(radius, area):
# #     radius = float(input("Enter the radius of the circle: "))
# #     area = 3.14159*radius*radius

# #     print("The area of the circle is" ,area)

# # def square_perimeter(side):
# #     return side * side

# # side1 = int(input("What is the side of the square?"))
# # print("The perimeter of the square is:", square_perimeter(side1))

# def circle_details(radius):
#     return 2 * 3.14 * radius, radius * radius * 3.14

# radius1 = float(input("What is the radius of the circle?"))
# print("Result:", circle_details(radius1))

import math

def geometry(side_length, radius):
    # Perimeter / circumference
    square_perimeter = 4 * side_length
    circle_circumference = 2 * math.pi * radius

    # Area
    square_area = side_length ** 2
    circle_area = math.pi * radius ** 2

    # Compare perimeters
    if square_perimeter > circle_circumference:
        print("The square has a larger perimeter.")
    elif circle_circumference > square_perimeter:
        print("The circle has a larger circumference.")
    else:
        print("The square and circle have equal perimeter/circumference.")

    # Compare areas
    if square_area > circle_area:
        print("The square has a larger area.")
    elif circle_area > square_area:
        print("The circle has a larger area.")
    else:
        print("The square and circle have equal area.")
