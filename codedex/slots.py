import random

symbols = ["🍒", "🍇", "🍉", "7️⃣"]

game_start = input("Do you want to play the slot machine? (Y/N): ").strip().upper()

while game_start == "Y":
    spin = random.choices(symbols, k=3)
    print(" | ".join(spin))

    if spin.count("7️⃣") == 3:
        print("JACKPOT! Three 7️⃣! 🎉")
    else:
        print("Better luck next time!")

    game_start = input("\nWant another spin? (Y/N): ").strip().upper()

print("Thanks for playing!")
