"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers typed by the user
# 2. Process: The program performs four arithmetic operations (addition, subtraction, multiplication, and division) on the two numbers.
# 3. Out: The results of the four arithmetic operations printed to the screen.
# 4. What happens when the second number is zero, and why: The program will calculate and display 
#    the results for addition, subtraction, and multiplication, but will display a text warning 
#    ("Cannot divide by zero") instead of attempting the division. I chose this approach because 
#    it prevents a ZeroDivisionError crash while still delivering the valid calculations for the other three operations.


# Your code below
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number:"))

print("The first number is : ", number_1)
print("The second number is : ", number_2)

# Addition
print(f"{number_1} + {number_2} = {number_1 + number_2}")

# Subtraction
print(f"{number_1} - {number_2} = {number_1 - number_2}")

# Multiplication
print(f"{number_1} * {number_2} = {number_1 * number_2}")

# Division (handling the zero case)
if number_2 != 0:
    division = number_1 / number_2
    print("The division of two numbers is:", division)
else:
    print("Cannot divide by zero")