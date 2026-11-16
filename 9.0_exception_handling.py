"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The user enters a number.

# 2. Process:
# The program divides 100 by the number entered.
# It checks if the user enters zero or an invalid value.
# If there is an error, it displays a message and asks again.
# The user gets 4 attempts to enter a valid number.

# 3. Out:
# The program displays the result of the division.
# If the input is invalid, it displays an error message.
# The program does not crash.

# 4. The two failures, and whether they deserve the same message:
# The first failure is ZeroDivisionError when the user enters zero.
# The second failure is ValueError when the user enters text
# or leaves the input empty.
# They should have different messages because they are different errors.
# Catching them separately helps the user understand the problem.



# Your code below
attempts = 4

for attempt in range(attempts):

    try:
        number = float(input("Enter a number: "))

        result = 100 / number

        print("Result:", result)
        break

    except ZeroDivisionError:
        print("You cannot divide by zero. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

else:
    print("You have used all 4 attempts.")

print("Program finished without crashing.")

