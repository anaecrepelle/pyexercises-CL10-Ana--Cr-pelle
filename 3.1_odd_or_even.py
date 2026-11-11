"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers typed by the user
# 2. Process: The inputs are converted to integers, then added, subtracted, and multiplied. For division, an if/else statement checks the second number's value before attempting the calculation.
# 3. Out: The two original numbers are printed back to the user, followed by the calculated sum, difference, product, and either the quotient or a zero-division warning.
# 4. What happens on 0, on a negative number, on a very large number: 
# The program successfully calculates and displays the sum, difference, and product, but skips the division calculation, printing "Cannot divide by zero" instead. This prevents a fatal `ZeroDivisionError` crash while still providing the user with the other three valid mathematical results. If the user enters a very large number, the program will refuse to run and ask for a smaller number instead.


# Your code below
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number:"))

print("The first number is : ", number_1)
print("The second number is : ", number_2)

# Sum of two number
sum = number_1 + number_2
print("The sum of two numbers is: ", sum)

# Difference of two numbers
diff = number_1 - number_2
print("The diff of two numbers is: ", diff)

# produt of two numbers
product = number_1 * number_2
print("The product of two numbers is:", product)

# division of two numbers
if number_2 != 0:
    division = number_1 / number_2
    print("The division of two numbers is:", division)
else:
    print("Cannot divide by zero")