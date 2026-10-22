songs = []

def add_song(songs):
    song_title = input("Enter Song Title: ")
    artist_name = input("Enter Artist Name: ")
    minutes = int(input("Enter Duration(Minutes): "))
    seconds = int(input("Enter Duration(Seconds): "))

    duration = minutes * 60 + seconds

    song = {
        "title": song_title,
        "artist": artist_name,
        "duration": duration,
        "plays": 0
    }

    songs.append(song)

    print("Success!")

    return songs


def record_listen(songs):
    song_title = input("Enter Song Title: ")

    for song in songs:
        if song["title"] == song_title:
            song["plays"] += 1
            print("Listen recorded!")
            return

    else:
        print("error. Song doesn't exist.")




def generate_wrapped(songs):
    if len(songs) == 0:
        print("No songs in your library!")
        return
    
    total_songs = len(songs)
    total_plays = 0
    total_seconds = 0
    most_played = songs[0]

    for song in songs:
        total_plays += song["plays"]
        total_seconds += song["duration"] * song["plays"]

        if song["plays"] > most_played["plays"]:
            most_played = song

    total_minutes = total_seconds // 60

    print("========== YOUR SPOTIFY WRAPPED ==========")
    print("Total Songs:", total_songs)
    print("Total Plays:", total_plays)
    print("Total Listening Time:", total_minutes, "minutes")

    if total_plays == 0:
        print("No songs have been played yet!")
    else:
        print("\nYour Most Played Song:")
        print(most_played["title"], "-", most_played["artist"], 
              "(",most_played["plays"], "plays)")

    print("==========================================")