"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of at least eight items (regional advertising budgets)
# 2. Process: The list is displayed in four different orders: ascending, descending, reversed, and shuffled. The original list is preserved by using copies for the reversed and shuffled orders, while the sorted orders return new lists without modifying the original.
# 3. Out: The original list, the four reordered lists (ascending, descending, reversed, shuffled), and a final proof that the original list remains unchanged.
# 4. My four orders, and which ones modify the original:
#    - Ascending (smallest to largest) using `sorted(list)`: This returns a new list and does NOT modify the original.
#    - Descending (largest to smallest) using `sorted(list, reverse=True)`: This returns a new list and does NOT modify the original.
#    - Reversed index order using `.reverse()`: This method modifies the list IN PLACE. To protect the original, I must create a copy of the list first, then reverse the copy.
#    - Random order using `random.shuffle()`: This method also modifies the list IN PLACE. Like `.reverse()`, I must apply it to a copy of the original list.


# Your code below
import random

# Original list from Exercise 4.0
regional_budgets = [1200, 3500, 800, 5400, 2100, 4300, 1500, 2900]
print(f"STARTING ORIGINAL: {regional_budgets}\n")

# 1. Ascending Order
ascending_budgets = sorted(regional_budgets)
print(f"1. Ascending:  {ascending_budgets}")

# 2. Descending Order
descending_budgets = sorted(regional_budgets, reverse=True)
print(f"2. Descending: {descending_budgets}")

# 3. Reversed Order (requires a copy because .reverse() modifies in place)
reversed_budgets = regional_budgets.copy()
reversed_budgets.reverse()
print(f"3. Reversed:   {reversed_budgets}")

# 4. Random Order (requires a copy because random.shuffle() modifies in place)
shuffled_budgets = regional_budgets.copy()
random.shuffle(shuffled_budgets)
print(f"4. Shuffled:   {shuffled_budgets}\n")

# PROOF: Displaying the original list to show it remains undamaged
print(f"PROOF ORIGINAL IS INTACT: {regional_budgets}")