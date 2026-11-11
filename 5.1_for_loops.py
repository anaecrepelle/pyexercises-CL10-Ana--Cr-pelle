"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of names
# 2. Process: Iterate through the list of names, compute the length of each name, and print the name along with its length.
# 3. Out: A printed line for each name in the list, showing the name and its length.
# 4. What I compute for each item, and why it is worth showing: I compute the length of each name to provide additional information about the names in the list. This can be useful for understanding the diversity of name lengths and for any further processing that may require knowledge of name lengths.


# Your code below
names = ["Anaé", "Pema", "Martina", "Tatiana", "Léa", "Agathe", "Sebastien", "Benjamin"]

print("List of names and their lengths:", names)

print("First item of the list is: ", names[0])
print("Second item of the list is: ", names[1])
print("Third item of the list is: ", names[2])

i = 1, 2, 3, 4, 5

for i in range(1, 10):
    print("Item", i)   

for i in names:
    length = len(i)
    print("Name: ", i, "Length:" , length)

    