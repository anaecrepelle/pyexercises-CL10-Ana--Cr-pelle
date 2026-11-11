"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of at least eight items
# 2. Process: The list is displayed in its entirety, a specific item is accessed by index, the list is sorted, and a computed value (average) is derived from the list.
# 3. Out: The original list, a selected item, the sorted list, and the computed average.
# 4. What my list is about, and what I computed from it: The list contains monthly regional advertising budgets. I computed the average budget to understand the typical spending level across regions.

# Your code below
number_1 = 2
number_2 = 4
number_3 = 6
number_4 = 8
number_5 = 10

print("The first number is : ", number_1)
print("The second number is : ", number_2)
print("The third number is : ", number_3)
print("The fourth number is : ", number_4)
print("The fifth number is : ", number_5)

numbers = [3, 5, 7, 9, 11, 13, 15, 17, 1, 2, 4, 6, 8, 10]
print("The whole list is : ", numbers)
print("The second item of the list is : ", numbers[1])
print("The first item of the list is : ", numbers[0])

sorted_list = sorted(numbers)
print("The sorted list is : ",  sorted_list)

removed_number = numbers.pop()
print("The removed item is : ", removed_number)
print("The list after removing the last item is : ", numbers)
print("The sorted list after removing the last item is : ", sorted_list)
removed_number_last = sorted_list.pop()
print("The removed item from the sorted list is : ", removed_number_last)
print("The sorted list after removing the last item is : ", sorted_list)

# List of 8 monthly regional advertising budgets
regional_budgets = [1200, 3500, 800, 5400, 2100, 4300, 1500, 2900]

print("--- Data Overview ---")

# Display the whole list
print(f"All regional budgets: {regional_budgets}")

# Display one item of my choice (e.g., the 3rd item / index 2)
print(f"Budget for our third region: €{regional_budgets[2]}")

# Display the list sorted
# Using sorted() creates a new sorted list without modifying the original
sorted_budgets = sorted(regional_budgets)
print(f"Budgets ordered from smallest to largest: {sorted_budgets}")

# Compute something from it: The average budget
average_budget = sum(regional_budgets) / len(regional_budgets)
print(f"Average regional budget: €{average_budget:.2f}")