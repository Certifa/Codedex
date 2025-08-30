import string
import random

accounts_passwords = {}


def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))


def show_accounts():
    if accounts_passwords:
        print("Overzicht van opgeslagen accounts en wachtwoorden:")
        for account, password in accounts_passwords.items():
            print(f"{account} - {password}")
    else:
        print("Nog geen accounts opgeslagen.")


def save_passwords_to_file(filename="pass.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for account, password in accounts_passwords.items():
            f.write(f"{account} - {password}\n")


def main():
    while True:
        show_accounts()
        account = input(
            "\nVoor welk account wil je een wachtwoord genereren? (of typ 'stop' om te stoppen): "
        )
        if account.lower() == "stop":
            break
        try:
            length = int(input("Hoe lang moet het wachtwoord zijn? "))
            password = generate_password(length)
            accounts_passwords[account] = password
            print(f"Je wachtwoord voor {account} is: {password}\n")
            save_passwords_to_file()  # Sla na elke wijziging op
        except ValueError:
            print("Ongeldige invoer. Voer een getal in.\n")


if __name__ == "__main__":
    main()
