"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in? 
# The program uses permissions for a marketing campaign.

    2. What happens to it?
# The program combines two permissions using OR.
# It checks for another permission using AND.
# It adds a permission using OR.
# It removes a permission using AND and NOT.

    3. What comes out? 
#The program displays the permissions in binary at each step.

    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.
# The permissions are for managing a marketing campaign.
# VIEW means someone can see the campaign.
# EDIT means someone can make changes.
# PUBLISH means someone can publish the campaign.


WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
VIEW = 0b001
EDIT = 0b010
PUBLISH = 0b100

permissions = VIEW | EDIT
print("Combined permissions:", bin(permissions))

has_publish = (permissions & PUBLISH) != 0
print("Can publish:", has_publish)
print("Current permissions:", bin(permissions))

permissions = permissions | PUBLISH
print("After adding publish:", bin(permissions))


permissions = permissions & ~EDIT
print("After removing edit:", bin(permissions))