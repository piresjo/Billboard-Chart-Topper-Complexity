import json

class SiteObject():
    def __init__(self):
        self.artists_and_songs = None
        self.artists_by_letter_dict = {}
        self.data_file_location = 'static/data/combinedArtistsAndSongs.json' 

    def processLetter(self, letter):
        letter = letter.lower()
        if self.artists_and_songs is None:
            with open(self.data_file_location, 'r') as json_file:
                artists_and_songs = json.load(json_file)
            self.artists_and_songs = artists_and_songs
        if letter.upper() not in self.artists_by_letter_dict:
            sorted_final_list = getArtistsByStartingChar(self.artists_and_songs, letter)
            self.artists_by_letter_dict[letter.upper()] = sorted_final_list

def getArtistsByStartingChar(artist_songs_list, starting_char):
    starting_char_upper = starting_char.upper()
    starting_char_lower = starting_char.lower()
    return [x for x in artist_songs_list if x[0][0] == starting_char_upper or x[0][0] == starting_char_lower]

def modifyDict(dictVal):
    songs = list(dictVal.keys())
    songsList = []
    for song in songs:
        songsList.append((song, dictVal[song]["top"], dictVal[song]["length"]))
    return songsList

def getArtistsSongsLengths(list_val):
    lengths = []
    artists = []
    songs = []
    for tuple_val in list_val:
        artists.append(tuple_val[0])
        songs.append(modifyDict(tuple_val[1]))
        lengths.append(len(tuple_val[1]))
    return (artists, songs, lengths)

