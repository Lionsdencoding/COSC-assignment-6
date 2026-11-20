"""
Filename: 13_Modules_Make_Assignment_main.py

The Geometry Calculator (Main Script)

This is the second of two files for your assignment. This file should be saved
as `main.py`. This is the script that the user will run.

Instructions:
Follow the steps outlined in the comments below to complete the program.
"""

# 1. Import your `geometry` module.
#    Make sure `geometry.py` is in the same folder as this file.

import geometry

# 2. Print a welcome message for the user.

print("Hello, welcome to the geometry calculator")

# 3. Ask the user for their choice of shape.
#    Store their answer in a variable. Use .lower() to make it case-insensitive.

shape = input("choose a shape (square, rectangle, circle): "). lower()

# 4. Use an if/elif/else block to determine which shape they chose.

# 5. If they chose "square":
#    a. Ask the user for the side length (and convert it to a float).
#    b. Call the `area_of_square` function from your geometry module.
#    c. Print the result in a user-friendly sentence.
if shape == "square":
  length = float(input("enter the length: "))
  area = geometry.area_of_square(side)
  print(f"the area of the square is {area}.")
# 6. If they chose "rectangle":
#    a. Ask the user for the length and width (as floats).
#    b. Call the `area_of_rectangle` function.
#    c. Print the result.
elif shape == "rectangle"
  length = float(input("enter the length: "))
  width = float(input("enter the width: "))
  area = geometry.area_of_rectangle(length, width)
  print(f"the area of the rectangle is {area}.")
# 7. If they chose "circle":
#    a. Ask for the radius (as a float).
#    b. Call the `area_of_circle` function.
#    c. Print the result, perhaps formatted to 2 decimal places.
elif shape == "circle"
  radius = float(input("enter the radius: "))
  area = geometry.area_of_circle(radius)
  print(f"the area of the square is {area.2f}.")
# 8. If they entered an invalid shape, print an error message.
else:
  print("error: this shape is invalid, choose a square, rectangle, or a circle.")
