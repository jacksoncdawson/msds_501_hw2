# DO NOT ADD LIBRARIES/PACKAGES.
# If you want to cover additional error cases other than the given below,
# feel free to create a error message.

spotify = {
    1: {"artists": ["ROSÉ", "Bruno Mars"], "title": "APT.", "length": "2:49"},
    2: {"artists": ["Lady Gaga", "Bruno Mars"], "title": "Die With a Smile",
        "length": "4:11"},
    3: {"artists": ["Ed Sheeran"], "title": "Sapphire", "length": "2:59"},
    4: {"artists": ["Billie Eilish"], "title": "Birds of a Feather",
        "length": "3:30"},
    5: {"artists": ["Benson Boone"], "title": "Beautiful Things",
        "length": "3:00"},
    6: {"artists": ["Sabrina Carpenter"], "title": "Manchild",
        "length": "3:33"},
    7: {"artists": ["Alex Warren"], "title": "Ordinary", "length": "3:06"},
    8: {"artists": ["Billie Eilish"], "title": "Wildflower", "length": "4:21"},
    9: {"artists": ["Sabrina Carpenter"], "title": "Espresso",
        "length": "2:55"},
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
        for artist in entry["artists"]: 
            artists.add(artist) 

    return ', '.join(sorted(list(artists)))

def song_by_ranking():
    
    # Input (Validation)
    try:
        request = int(input(ranking_question).strip())
    except ValueError:
        return ranking_value_error
        
    if (request > 10) or (request < 1):
        return ranking_range_error
    
    entry = spotify[request]
    artists = ', '.join(entry["artists"])
    title = entry["title"]

    return f'{request}: {title} by {artists}'

def songs_by_artist():
    request = input(artist_question).lower()
    songs = {}
    for i in spotify:
        entry = spotify[i]
        for artist in entry["artists"]:
            if artist.lower() == request:
                songs[i] = entry["title"]
                
    if len(songs) == 0:
        return artist_error + request.strip().title()
    else:
        return '\n'.join(f"{rank}: {title}" for rank, title in songs.items())

def songs_by_length():

    # Input (Validation)
    try:
        request = int(input(length_question).strip())
    except ValueError:
        return length_value_error
    
    entries = []
    for entry in spotify.values():
        entry_copy = entry.copy()
        mins, sec = entry_copy['length'].split(':')
        entry_copy['length'] = int(mins)*60 + int(sec)
        entries.append(entry_copy)
    
    if request < 0:
        entries.sort(key=lambda entry: entry['length'])
    elif request >= 0:
        entries.sort(key=lambda entry: entry['length'], reverse=True)
    
    # Prepare output
    output = []
    for entry in entries[:abs(request)]:
        artists = ', '.join(entry['artists'])
        title = entry['title']
        length = entry['length']
        output.append(f"{title} by {artists} ({length} seconds)")
    return '\n'.join(output)

def main():

    exit = False
    
    while not exit:

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
            exit = True
        else:
            continue

main()

