file = open("example.txt", "w")

file.write("Hello, World!\n")
file.write("Does this actually work\n")
file.write("Baaaah")

file = open("example.txt", "r")

content = file.read()

print(content)

line1 = file.readline()  # Read the first line
print(line1, end="")  # Printing the first line

line2 = file.readline()  # Read the second line
print(line2, end="")  # Printing the second line

lines = file.readlines()

for line in lines:
    print(line, end="")  # The .readlines() method lets you read all lines in a list:

# Opens file to read
file = open("filename.txt", "r")

# Closes file
file.close()

# with open('filename', 'r') as f:
# handle file here
