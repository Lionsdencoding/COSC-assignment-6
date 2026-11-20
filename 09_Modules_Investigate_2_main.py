"""
Filename: 09_Modules_Investigate_2_main.py

Instructions:
This script imports `08_Modules_Investigate_2_messy_module.py`.
Run this script and observe the output.

Answer the following questions:

1.  This file only has three lines of code. Why was "This message runs
    on import!" printed to the screen?

the import messy_module executes all the top-level code from top to bottom. The print statement at the module level is regarded
as the top-level code, so it is ran immediately during the import, this happens even thoughj messy_modules ins only called
later with useful_function()

2.  When does the code inside `messy_module.py` get executed?

The code inside messy_module gets executed the moment that "import messy_module" gets reached by the program and all of its code
then gets ran top to bottom before resuming the next line in the importing script.

3.  Section 7.3 in the textbook discusses a special `if` statement that can
    prevent this side effect. What is that `if` statement, and how would you
    use it in `messy_module.py` to stop the message from printing on import?

the special if statement that can prevent this side effect is the "if __name__ == "__main__":" guard.
you would run the if statement 
"""

print("Main program is about to import...")

# The code in messy_module.py runs at this line!
import messy_module

print("Main program has finished importing.")

# We can still use the functions from the module
messy_module.useful_function()
