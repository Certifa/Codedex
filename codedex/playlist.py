# Write code below 💖

# 💿 Theme: Indie Travel Songs
import time

playlist = [
    "Porches - rangerover",
    "Mount Eerie - You Swan, Go On",
    "Carolyn Polachek - Look at Me Now",
    "Pinegrove - Darkness",
    "LVL UP - Spirit Was",
    "Mitski - First Love / Late Spring",
]

yes_or_no = int(
    input(
        """ 
========================================
Hi! Do you want to add or remove a song?
========================================

1) Add
2) Remove
"""
    )
)

if yes_or_no == 1:
    print("\nHere is the list of songs:")
    time.sleep(1)

    song_choice = ""

    while song_choice != "no":
        # Toon playlist vóór input
        print("\n🎵 Current Playlist:")
        for song in playlist:
            print(f"- {song}")

        song_choice = input("\nWhat song do you want to add? (type 'no' to stop): ")

        if song_choice == "no":
            print("\nGoodbye! 👋")
            break

        playlist.append(song_choice)
        print(f"\n✅ '{song_choice}' has been updated.")

if yes_or_no == 2:
    print("\nHere is the list of songs:")
    time.sleep(1)

    song_remove = ""

    while song_remove != "no":
        # Toon playlist vóór input
        print("\n🎵 Current Playlist:")
        for song in playlist:
            print(f"- {song}")

        # Vraag om input
        song_remove = input("\nWhich song do you want to remove? (type 'no' to stop): ")

        # Als het 'no' is, stop
        if song_remove == "no":
            print("\nGoodbye! 👋")
            break

        # Check of het liedje bestaat in de lijst
        if song_remove in playlist:
            playlist.remove(song_remove)
            print(f"\n✅ '{song_remove}' has been removed.")
        else:
            print(f"\n❌ '{song_remove}' is not in the playlist.")
