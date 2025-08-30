# Write code below 💖

Q1 = int(input("Q1| Do you like Dawn or Dusk? \n\n" " 1) Dawn \n" " 2) Dusk \n\n"))
Q2 = int(input("\n Q2| When I'm dead, I want people to remember me as: \n\n" " 1) The Good \n" " 2) The Great \n" " 3) The Wise \n" " 4) The Bold \n\n" ))
Q3 = int(input("\n Q3| Which kind of instrument most pleases your ear? \n\n" " 1) The violin \n" " 2) The trumpet \n" " 3) The piano \n" " 4) The drum \n\n"))

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

if Q1 == 1:
  Gryffindor +=1
  Ravenclaw +=1
elif Q1 == 2:
  Hufflepuff +=1  
  Slytherin +=1
else:
  print("Wrong input.")

if Q2 == 1:
  Hufflepuff +=2
elif Q2 == 2:
  Slytherin +=2
elif Q2 == 3:
  Ravenclaw +=2
elif Q2 == 4:
  Gryffindor +=2
else:
  print("Wrong input")

if Q3 == 1:
  Slytherin += 4
elif Q3 == 2:
  Hufflepuff +=4
elif Q3 == 3:
  Ravenclaw +=4
elif Q3 == 4:
  Gryffindor +=4
else:
  print("Wrong input")


if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print("Gryffindor wins!")
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print("Ravenclaw wins!")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print("Hufflepuff wins!")
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
    print("Slytherin wins!")
else:
    print("It's a tie!")
