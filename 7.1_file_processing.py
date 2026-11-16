"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.
    
ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Some names are written in lowercase letters.
# - Some names are written in uppercase letters.
# - Some lines have extra spaces at the beginning.
# - There are empty lines between names.
# - The names are not sorted by last name.

# 1. In: # The program reads names from names.txt.

# 2. Process, problem by problem:
# Remove empty lines using strip().
# Remove extra spaces using split() and join().
# Fix capitalization using title().
# Sort the names alphabetically by last name.
# Save the cleaned names in a new file.

# 3. Out: 
# A new file called cleaned_names.txt containing
# cleaned names sorted by last name.
# The original names.txt file stays unchanged.

# 4. How I decide which word is the last name:
# The last name is usually the last word in each line.
# For example, in "Ada Lovelace", Lovelace is the last name.
# For "Guido van Rossum", I treat "van Rossum" as the surname.
# I sort names alphabetically without considering capitalization.


# Your code below

with open("names.txt", "r", encoding="utf-8") as file:
    names = file.readlines()

cleaned_names = []

for name in names:
    name = " ".join(name.split())

    if name:
        name = name.title()
        name = name.replace("Van Rossum", "van Rossum")
        cleaned_names.append(name)

# Create a function to find the last name
def get_last_name(name):
    if name.lower().endswith("van rossum"):
        return "van rossum"
    return name.split()[-1].lower()

# Sort the names by last name
cleaned_names.sort(key=get_last_name)

# Save the cleaned names in a new file
with open("cleaned_names.txt", "w", encoding="utf-8") as file:
    for name in cleaned_names:
        file.write(name + "\n")

# Display the cleaned names
print("Cleaned and sorted names:")

for name in cleaned_names:
    print(name)

# Count the original lines and cleaned lines
print("Original lines:", len(names))
print("Cleaned lines:", len(cleaned_names))

# Display the first and last names
print("First name in sorted list:", cleaned_names[0])
print("Last name in sorted list:", cleaned_names[-1])
