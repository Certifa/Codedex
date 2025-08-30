while True:
    print("Choose + or -, or q to quit: ")
    choice = input()
    
    if choice not in ["+", "-", "q"]:
        print("Invalid choice. Please enter + or - or q to quit.")
        continue

    if choice == "q":  
        print("Goodbye!")
        break 

        
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    

    if choice == "+":
        def add(a, b):
            return a + b
        print("Addition:", add(num1, num2))
    elif choice == "-":
        def subtract(a, b):
            return a - b
        print("Subtraction:", subtract(num1, num2))

# * The code above is a simple calculator that can add and subtract numbers. The user is prompted to enter a choice of + or - or q to quit. If the user enters q, the program will print "Goodbye!" and exit. If the user enters +, the program will prompt the user to enter two numbers and then print the sum of the two numbers. If the user enters -, the program will prompt the user to enter two numbers and then print the difference of the two numbers. The program will continue to prompt the user for input until the user enters q to quit.