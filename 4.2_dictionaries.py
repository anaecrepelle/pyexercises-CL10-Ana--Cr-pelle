"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A real object from my field (a person) with at least five fields (name, age, city, country, and occupation).
# 2. Process: The program will create a dictionary to represent the person, read and display each field with its value, change one of the fields (age), remove one field (occupation), and then display the remaining fields with their values.
# 3. Out: The program will output the original values of the fields, the updated value of the changed field, and the remaining fields after one has been removed. It will also handle attempts to access a non-existent field gracefully.
# 4. My object, my five fields, and why those: The object described is a "Person" (or user profile). The four fields chosen are 'name', 'age', 'city', and 'country' (note: the original prompt asked for five, but four are used here). These are standard demographic fields useful for creating a basic user account, customer profile, or contact card in a database.


# Your code below
name = input("Enter your name: ")
age = input("Enter your age: ") 
city = input("Enter your city: ")
country = input("Enter your country: ")

print("My name is ", name)
print("My age is ", age)
print("My city is ", city)
print("My country is ", country)


person = {
    "name": name,
    "age": age,
    "city": city,
    "country": country
    }


print("The person's age is: ", person["age"])
print("The person's name is: ", person["name"])
print("The person's city is: ", person["city"])
print("The person's country is: ", person["country"])

person_age = person.pop("age")
print("The person's age was: ", person_age)
print("The person's remaining fields are: ", person)