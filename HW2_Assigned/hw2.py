# DO NOT ADD LIBRARIES/PACKAGES.
# If you want to cover additional error cases other than the given below,
# feel free to create a error message.

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
    artists = set()
    for entry in spotify.values(): 
        artists.update(entry["artists"]) # Instead of looping through artists manually
    return ', '.join(sorted(artists)) # no need to explicitly convert to list - sorted does this implicitly with sets

def song_by_ranking():
    
    # Input (Validation)
    try:
        rank = int(input(ranking_question).strip())
    except ValueError:
        return ranking_value_error # return the correct string, but let main() decide what to do with it
        
    if (rank > 10) or (rank < 1): 
        return ranking_range_error # return the correct string, but let main() decide what to do with it
    
    entry = spotify[rank]
    artists = ', '.join(entry["artists"])
    title = entry["title"]

    return f'{rank}: {title} by {artists}'

def songs_by_artist():
    artist_name = input(artist_question).strip().lower()
    found = False
    ret = ""
    
    for rank, song in spotify.items():
        
        if any(artist_name in artist.lower() for artist in song["artists"]):
            ret += (f"{rank}: {song["title"]}\n")
            found = True
    
    if not found:
        return artist_error + artist_name.strip().title()
    
    return ret.strip()

def songs_by_length():

    # Input (Validation)
    try:
        num_songs = int(input(length_question).strip())
    except ValueError:
        return length_value_error
    
    def to_seconds(length_str):
        minutes, seconds = map(int, length_str.split(":"))
        return minutes * 60 + seconds

    songs = []
    for song in spotify.values():
        total_seconds = to_seconds(song["length"])
        songs.append((song["title"], song["artists"], total_seconds))
        
    songs.sort(key=lambda x: x[2], reverse=num_songs>0)
    
    # prepare output
    ret = ""
    for title, artists, seconds in songs[:abs(num_songs)]:
        ret += f"{title} by {', '.join(artists)} ({seconds} seconds)\n"
    
    return ret.strip()

def main():
    
    while True:

        # Input (Validation)
        try:
            selection = int(input(user_choice_question).strip())
        except ValueError:
            continue
        
        if selection == 1:
            print(list_artists())
        elif selection == 2:
            print(song_by_ranking())
        elif selection == 3:
            print(songs_by_artist())
        elif selection == 4:
            print(songs_by_length())
        elif selection == 0:
            break
        else:
            continue

main()

