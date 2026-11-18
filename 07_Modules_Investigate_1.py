"""
Filename: 07_Modules_Investigate_1.py

Instructions:
This program uses the `math` module, which is built into Python.
Run the code and observe the output.

Answer the following questions:

1.  What does the line `import math` do? What does it make available to
    our program?
The line 'import math' imports the math module and beinds the module object tot the name math in the current programs space.
This module makes functions such as sqrt, sin, cos, facotrials, etc, as well as constanst like pi, e, tau, etc accessible to be used by the program

2.  Why do we have to write `math.pi` and `math.sqrt()` instead of just
    `pi` and `sqrt()`? What is the purpose of the `math.` prefix?

The purpose of the 'math' prefix is to call on the attribute attributed to that module's library.

3.  The `math` module contains dozens of other functions and constants.
    How could you find out what other tools are in the `math` module?
    (Hint: Think about Section 7.4 of the textbook).

    To find out what other tools are in the 'math' module use the built in dir() and help() functions and put the name of the module
    AKA 'math' in the parenthesis help(math) or print(dir(math))
"""

# To use special math functions and constants, we must first import the module.
import math

def circle_circumference(radius):
    """Calculates the circumference of a circle."""
    # We use the constant 'pi' from the math module.
    return 2 * math.pi * radius

def hypotenuse(a, b):
    """Calculates the hypotenuse of a right triangle using Pythagorean theorem."""
    # We use the square root function 'sqrt' from the math module.
    return math.sqrt(a**2 + b**2)


# --- Main program execution ---
radius = 10
circumference = circle_circumference(radius)
print(f"A circle with radius {radius} has a circumference of {circumference:.2f}.")

side1 = 3
side2 = 4
hyp = hypotenuse(side1, side2)
print(f"A right triangle with sides {side1} and {side2} has a hypotenuse of {hyp}.")
