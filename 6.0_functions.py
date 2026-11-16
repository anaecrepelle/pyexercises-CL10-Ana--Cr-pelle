"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of numbers
# 2. Process: The function will take the list of numbers as input, iterate through the list, and compute the sum of the numbers. It will then return the computed sum.
# 3. Out: a single number representing the sum of the input list
# 4. My function name, and why return rather than print: 
# Function name: `add_numbers`. The name clearly indicates that the function is responsible for adding two numbers together. It is descriptive and conveys the purpose of the function without needing to read the code.
# Return vs. Print: `print` only displays text on the screen for a human to read, but the data is then lost. `return` actually hands the computed data back to the program so it can be stored in a variable, used in further calculations, or saved to a database.


# Your code below
number_1 = 5
number_2 = 10

sum = number_1 + number_2
print("The sum of", number_1, "and", number_2, "is:", sum)

number_1 = 4
number_2 = 3

sum = number_1 + number_2
print("The sum of", number_1, "and", number_2, "is:", sum)

num1 = 10
num2 = 20

def add_numbers(num1, num2):
    sum_result = num1 + num2
    return sum_result

sum1 = add_numbers(10, 20)
print("The sum of 10 and 20 is:", sum1)

sum2 = add_numbers(4, 3)
print("The sum of 4 and 3 is:", sum2)

sum3 = add_numbers(7, 2)
print("The sum of 7 and 2 is:", sum3)
