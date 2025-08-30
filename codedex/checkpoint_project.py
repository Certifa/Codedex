import random
import time

computer = random.randint(1, 5)

player = int(
    input(
        """
================================
Rock Paper Scissors Lizard Spock
================================

1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖

Pick a number: """
    )
)

choice = {
    1: "✊",
    2: "✋",
    3: "✌️",
    4: "🦎",
    5: "🖖",
}

print(f"You chose: {choice[player]}")
print(f"Computer chose: {choice[computer]}")

time.sleep(0.5)

if player == computer:
    print("It's a tie!")
elif (
    (player == 2 and computer == 3)
    or (player == 2 and computer == 1)
    or (player == 1 and computer == 4)
    or (player == 4 and computer == 5)
    or (player == 5 and computer == 3)
    or (player == 3 and computer == 4)
    or (player == 4 and computer == 2)
    or (player == 2 and computer == 5)
    or (player == 5 and computer == 1)
    or (player == 1 and computer == 3)
):
    print("You won!")
else:
    print("You lost.")
