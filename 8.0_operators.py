"""Exercise 8.0 — Operators (bonus, not graded)



WHAT THE PROGRAM MUST DO

Take two values of your choice and display, as a readable table, the result of every

comparison between them and of the logical combinations of those results.



ANSWER THESE FIRST, in comments

What goes in?
2. What happens to it?

3. What comes out?

4. Which two values did you pick, and which comparison result surprised you?



WHAT THE AI CANNOT KNOW

Your two values. Pick a pair where the answer is not obvious: two strings with

different capitalisation, a number and the same number written as text, or zero and

an empty string.



CHECK IT YOURSELF

Predict each result before running. Count how many you got right.



DELIVERABLE

This file, with your comments and your code.

"""



# Your code below 
a = 10
b = "10"

b_number = int(b)

print("Value 1:", a)
print("Value 2:", b)

print("\nComparison Table")
print("-" * 45)
print(f"{'Comparison':<30} {'Result'}")
print("-" * 45)

print(f"{'a == b':<30} {a == b}")
print(f"{'a != b':<30} {a != b}")

print(f"{'a > int(b)':<30} {a > b_number}")
print(f"{'a < int(b)':<30} {a < b_number}")
print(f"{'a >= int(b)':<30} {a >= b_number}")
print(f"{'a <= int(b)':<30} {a <= b_number}")

result1 = a == b
result2 = a != b

print("\nLogical Operators")
print("-" * 45)
print(f"{'Logical Operation':<30} {'Result'}")
print("-" * 45)

print(f"{'result1 and result2':<30} {result1 and result2}")
print(f"{'result1 or result2':<30} {result1 or result2}")
print(f"{'not result1':<30} {not result1}")
print(f"{'not result2':<30} {not result2}")