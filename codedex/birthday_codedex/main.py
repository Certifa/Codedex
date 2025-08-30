import datetime

import bday_messages

today = datetime.date.today()  # year, month, day
next_birthday = datetime.date(2025, 12, 6)

days_away = (next_birthday - today).days

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"My birthday is {days_away} days away!")
