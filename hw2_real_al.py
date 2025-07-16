spotify = {
    1: {"artists": ["ROSÉ", "Bruno Mars"], "title": "APT.", "length": "2:49"},
    2: {"artists": ["Lady Gaga", "Bruno Mars"], "title": "Die With a Smile", "length": "4:11"},
    3: {"artists": ["Ed Sheeran"], "title": "Sapphire", "length": "2:59"},
    4: {"artists": ["Billie Eilish"], "title": "Birds of a Feather", "length": "3:30"},
    5: {"artists": ["Benson Boone"], "title": "Beautiful Things", "length": "3:00"},
    6: {"artists": ["Sabrina Carpenter"], "title": "Manchild", "length": "3:33"},
    7: {"artists": ["Alex Warren"], "title": "Ordinary", "length": "3:06"},
    8: {"artists": ["Billie Eilish"], "title": "Wildflower", "length": "4:21"},
    9: {"artists": ["Sabrina Carpenter"], "title": "Espresso", "length": "2:55"},
    10: {"artists": ["Lady Gaga"], "title": "Abracadabra", "length": "3:43"}
}

user_choice_question = "Enter what you would like to browse:\n \
                        \t1: A list of artists in the top 10 most played songs\n \
                        \t2: Song details by ranking\n \
                        \t3: Songs by an artist\n \
                        \t4: Songs ordered by length\n \
                        \t0: Exit\n"

ranking_question = "Enter the ranking you're interested in (between 1 and 10): "
ranking_value_error = "Invalid input. Please enter a number."
ranking_range_error = "Ranking out of range."

artist_question = "Enter the name of the artist you're interested in: "
artist_error = "No songs were found by "

length_question = "Enter a number to view songs by length. (Positive: longest songs, Negative: shortest songs): "
length_value_error = "Invalid vallue. Please enter a number."


def list_artists():
    artist_set = set()
    for song in spotify.values():
        artist_set.update(song["artists"])
    print(', '.join(sorted(artist_set)))


def song_by_ranking():
    try:
        rank = int(input(ranking_question).strip())
    except ValueError:
        print(ranking_value_error)
        return
    if rank < 1 or rank > 10:
        print(ranking_range_error)
        return
    song = spotify[rank]
    artists = ', '.join(song["artists"])
    print(f"{rank}: {song['title']} by {artists}")


def songs_by_artist():
    name = input(artist_question).strip().lower()
    found = False
    for rank, song in spotify.items():
        if any(name == artist.lower() for artist in song["artists"]):
            print(f"{rank}: {song['title']}")
            found = True
    if not found:
        print(artist_error + name.title())


def songs_by_length():
    try:
        n = int(input(length_question).strip())
    except ValueError:
        print(length_value_error)
        return

    def to_seconds(length_str):
        minutes, seconds = map(int, length_str.split(":"))
        return minutes * 60 + seconds

    songs = []
    for song in spotify.values():
        total_seconds = to_seconds(song["length"])
        songs.append((song["title"], song["artists"], total_seconds))

    songs.sort(key=lambda x: x[2], reverse=n > 0)

    for title, artists, seconds in songs[:abs(n)]:
        print(f"{title} by {', '.join(artists)} ({seconds} seconds)")


def main():
    while True:
        try:
            choice = int(input(user_choice_question).strip())
        except ValueError:
            continue

        if choice == 1:
            list_artists()
        elif choice == 2:
            song_by_ranking()
        elif choice == 3:
            songs_by_artist()
        elif choice == 4:
            songs_by_length()
        elif choice == 0:
            break
        else:
            continue

main()