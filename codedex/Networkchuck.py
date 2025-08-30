print("Hello, welcome to Mike's Coffee Shop!")

name = input("What is your name?\n")


if name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("You're not welcome here Evil Ben!! Get out!!")
        exit()
    else:
        print("Oh, so you're one of those good Bens. Come on in!!")
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

# quantity = input("How many coffees would you like?\n")

if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    whipped_cream = input("Would you like whipped cream?\n")
    if whipped_cream == "Yes":
        price = 11
    else:
        price = 9
elif order == "Cappucino":
    price = 10
else:
    print("Sorry, we don't have that here.")
    price = 0

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

print(
    "Sounds good " + name + ", we'll have that " + order + " ready for you in a moment."
)
