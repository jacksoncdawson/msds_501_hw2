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

while True:
    try:
        user_choice_question = int(input("Enter what you would like to browse:\n \
                        \t1: A list of artists in the top 10 most played songs\n \
                        \t2: Song by ranking\n \
                        \t3: Songs by an artist\n \
                        \t4: Songs ordered by length\n \
                        \t0: Exit\n"))
    
    except ValueError:
        print("Invalid input")
        continue

    if int(user_choice_question) == 1:
        artists_set = set()
        for rank, info in spotify.items():
            for name in info['artists']:
                artists_set.add(name)
        artists_set = list(artists_set)
        artists_set.sort()
        print(', '.join(artists_set))
        continue

    elif int(user_choice_question) == 2:
        ranking_value_error = "Invalid input. Please enter a number."
        ranking_range_error = "Ranking out of range."
        while True:
            try:
                ranking_question = int(input("Enter the ranking you're interested in (between 1 and 10): "))
            except ValueError:
                print(ranking_value_error)
                break
            if ranking_question in range(1,11):
                print(f"{ranking_question}: {spotify[ranking_question]['title']} by {', '.join(spotify[ranking_question]['artists'])}")
                break
            else:
                print(ranking_range_error)
                break
        continue

    elif int(user_choice_question) == 3:
        artist_error = "No songs were found by "
        artist_question = input("Enter the name of the artist you're interested in: ")
        name_lst = list()
        for i in artist_question.split():
            i = i[0].upper() + i[1:].lower()
            name_lst.append(i)
        name = ' '.join(name_lst)
        count = 0
        for rank, info in spotify.items():
            if name in info['artists']:
                print(f"{rank}: {info['title']}")
                count += 1
        if count == 0:
            print(f'{artist_error}{artist_question}')
        continue

    elif int(user_choice_question) == 4:
        length_value_error = "Invalid vallue. Please enter a number."
        try:
            request = int(input("Enter a number to view songs by length. (Positive: longest songs, Negative: shortest songs): ").strip())
        except ValueError:
            print(length_value_error)
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
        output = []
        for entry in entries[:abs(request)]:
            artists = ', '.join(entry['artists'])
            title = entry['title']
            length = entry['length']
            output.append(f"{title} by {artists} ({length} seconds)")
        print('\n'.join(output))
        continue

    elif int(user_choice_question) == 0:
        break
    

