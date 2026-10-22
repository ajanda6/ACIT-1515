songs = [
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "duration": 200,
        "plays": 5
    },
    {
        "title": "Numb",
        "artist": "Linkin Park",
        "duration": 187,
        "plays": 8
    },
    {
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "duration": 234,
        "plays": 3
    }
]

# one example of how you can import the functions
from spotify import add_song, record_listen, generate_wrapped

def main():
    while True:
        print("\n====== SPOTIFY WRAPPED ======")
        print("1. Add a song")
        print("2. Record a listen")
        print("3. Generate Spotify Wrapped")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_song(songs)

        elif choice == "2":
            record_listen(songs)

        elif choice == "3":
            generate_wrapped(songs)

        elif choice == "4":
            print("Bye!")
            break

        else:
            print("Invalid choice. Try again.")

main()