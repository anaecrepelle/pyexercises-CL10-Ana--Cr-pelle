"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: ask the user for the following information: first name, last name, date of birth, and student number.
# 2. Process: save the information to a CSV file, appending it to the file if it already exists, and creating a header line if the file does not exist yet.
# 3. Out, file name and columns: The output file is named "7.0_student_data.csv" and it contains the following columns: First Name, Last Name, Date of Birth, Student Number.
# 4. Why these columns, and what this file is for: These columns were chosen to collect basic personal information about students. The file can be used for record-keeping, tracking student information, and potentially for administrative purposes such as enrollment or contact information management. Once the file has two hundred rows, it can serve as a database for student records, allowing for easy access and organization of student data.


# Your code below
print("Please enter the following information to record an entry:")
first_name = input("First Name: ")
last_name = input("Last Name: ")
birth = input("Date of Birth (YYYY-MM-DD): ")
student_number = input("Student number: ")

with open("7.0_student_data.csv", "a" , newline="") as file:
    file.write("First Name,Last Name,Date of Birth,Student Number\n")
    file.write(first_name + "," + last_name + "," + birth + "," + student_number + "\n")

print("Data saved successfully!")

