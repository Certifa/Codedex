weight = float(input("Hi! What is the weight of your Earth? "))
number = int(input("What is the planet number? "))

gravity = {
    1: 0.38,  # Mercury
    2: 0.91,  # Venus
    3: 0.38,  # Mars
    4: 2.53,  # Jupiter
    5: 1.07,  # Saturn
    6: 0.89,  # Uranus
    7: 1.14,  # Neptune
}

if number in gravity:
    print(f"Here you go! {weight * gravity[number]}")
else:
    print("Invalid planet number")
# The code calculates the weight of an object on different planets based on its weight on Earth.