"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
1. What goes in?
# The user enters a name, age, and student ID.

2. What happens to it?
# The program checks each value using regular expressions.
# It only saves the information if all three values are valid.
# If any value is wrong, the program displays an error message.

3. What comes out?
# The program saves valid information in student_details.csv.
# Invalid information is not saved.

4. What are your three fields, and what makes a value acceptable for each? Write the rule in plain English before writing any pattern.
# Name: Must contain only letters and spaces, from 2 to 30 characters.
# Age: Must be a whole number between 1 and 99, without a leading zero.
# Student ID: Must start with ST followed by exactly 4 digits.

# Pattern explanation:
# ^ means the beginning of the text.
# $ means the end of the text.
# [A-Za-z ] allows uppercase letters, lowercase letters, and spaces.
# {2,30} means between 2 and 30 characters.
# [1-9][0-9]? means a number from 1 to 99.
# ST means the ID must begin with those two capital letters.
# [0-9]{4} means exactly four digits.


WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below

import re
import csv

def valid_name(name):
    return re.fullmatch(r"[A-Za-z ]{2,30}", name) is not None


def valid_age(age):
    return re.fullmatch(r"[1-9][0-9]?", age) is not None


def valid_student_id(student_id):
    return re.fullmatch(r"ST[0-9]{4}", student_id) is not None




print("Name tests:")
print(valid_name("Alice"))
print(valid_name("A1"))
print(valid_name("123"))


print("Age tests:")
print(valid_age("20"))
print(valid_age("0"))
print(valid_age("abc"))


print("Student ID tests:")
print(valid_student_id("ST1234"))
print(valid_student_id("ST12"))
print(valid_student_id("AB1234"))


name = input("Enter your name: ").strip()
age = input("Enter your age: ").strip()
student_id = input("Enter your student ID: ").strip()


if valid_name(name) and valid_age(age) and valid_student_id(student_id):

    with open("student_details.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Name", "Age", "Student ID"])

        writer.writerow([name, age, student_id])

    print("Information saved successfully!")

else:
    print("Invalid information. Nothing was saved.")

    if not valid_name(name):
        print("Invalid name.")

    if not valid_age(age):
        print("Invalid age.")

    if not valid_student_id(student_id):
        print("Invalid student ID.")
