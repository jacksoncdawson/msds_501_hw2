# DO NOT ADD LIBRARIES/PACKAGES.

spotify = {
    1: {"artists": ["ROSÉ", "Bruno Mars"], "title": "APT.", "length": "2:49"},
    2: {"artists": ["Lady Gaga", "Bruno Mars"], "title": "Die With a Smile", "length": "4:11"},
    3: {"artists": ["Ed Sheeran"], "title": "Sapphire", "length": "2:59"},
    4: {"artists": ["Billie Eilish"], "title": "Birds of a Feather", "length": "3:30"},
    5: {"artists": ["Benson Boone"], "title": "Beautiful Things", "length": "3:00"},
    6: {"artists": ["Sabrina Carpenter"], "title": "Manchild", "length": "3:33"},
    7: {"artists": ["Alex Warren"], "title": "Ordinary", "length": "3:06"},
    8: {"artists": ["Billie Eilish"], "title": "Wildflower", "length": "4:21"},
    9: {"artists": ["Ed Sheeran"], "title": "Thinking Out Loud", "length": "3:34"},
    10: {"artists": ["Lady Gaga"], "title": "Abracadabra", "length": "3:43"}
}

def main():
    while True:
        print("Enter what you would like to browse:\n \
\t1: A list of artists in the top 10 most played songs\n \
\t2: Song by ranking\n \
\t3: Songs by an artist\n \
\t4: Songs ordered by length\n \
\t0: Exit\n")

        choice = input().strip()

        if choice == "0":
            break

        elif choice == "1":
            artists = set()
            for song in spotify.values():
                for artist in song["artists"]:
                    artists.add(artist)
            print(", ".join(sorted(artists)))

        elif choice == "2":
            print("Enter the ranking you're interested in (between 1 and 10): ")
            user_input = input().strip()
            try:
                rank = int(user_input)
                if rank < 1 or rank > 10:
                    print("Ranking out of range.")
                else:
                    song = spotify[rank]
                    print(f"{rank}: {song['title']} by {', '.join(song['artists'])}")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
