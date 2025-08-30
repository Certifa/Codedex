# Beginner notes

# TODO: Fix this function
# BUG: This is broken
# ! Important message
# * Green note
# ? Questionable logic here


print("Hello World!")

print("""Yes with 3 times the qoutations you can
      talk with a big message""")

print("You can add " + "sentences to" + " each other")

print("And you can add \n" + "new lines aswell!")

# Numeric variables - hold integers and decimal values
age = 25
temperature = 98.6

# String variables - Stores a sequence of characters enclosed in single or double quotes
name = "John Doe"
message = "Hello, world!"

# Boolean variables - only hold the values true and false
is_true = True
is_false = False

# List variables - Stores a collection of items, which can be of different types.
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]

# Tuple variables
coordinates = (10, 20)

# Dictionary variables
person = {"name": "Alice", "age": 30}

# Set variables
unique_numbers = {1, 2, 3}

# None variable
empty_value = None

# * Network chuck EP 2

# * len() function returns the length of a string or list or any other data type that has a length
len("Hello")

name = "CodeChef"
lowercase_name = name.lower()
uppercase_name = name.upper()
print(lowercase_name)  # Output: codechef
print(uppercase_name)  # Output: CODECHEF

print("Hello, welcome to the shop")

input("What is your name?")

print("Hello ...., thankyou for your order")

name = input("What is your name?\n")

print("Hello " + name + ",thankyou for your order")

for i in range(1, 6):
    print(i, "-", i * i)


for i in range(4):
    print("****")

# * For i in range (4) means that the loop will run 4 times

# * Network chuck EP 3

name = "Mike"

age = 23

# * to make a string into a number you can use int() or float(), and to make a number into a string you can use str()
Variablename = input("Enter a number: ")
int(Variablename)
print(Variablename)


print("Hello, welcome to Mike's Coffee Shop!")

name = input("What is your name?\n")

if name == "Ben":
    print("You're not welcome here Evil Ben!! Get out!!")
    exit()
else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n")

# People with beards longer then 1 inch can skip the line below

beard_length = int(input("How long is your beard, in inches?\n"))

if beard_length >= 1:
    print("Oh, hello good sir, nice beard. You may go to the front of the line.\n")

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

print(
    name
    + ", what would you like from our menu today? Here is what we are serving.\n"
    + menu
)

# Frapuccino is a specialty item

order = input()

quantity = input("How many coffees would you like?\n")

if order == "Frappuccino":
    price = 13
else:
    price = 8

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

print(
    "Sounds good " + name + ", we'll have that " + order + " ready for you in a moment."
)

print("Hello {name}, thankyou for your order")
