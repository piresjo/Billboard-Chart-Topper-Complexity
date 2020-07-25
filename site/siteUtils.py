import json

class SiteObject():
    def __init__(self):
        self.artists_and_songs = None
        self.artists_by_letter_dict = {}

def getArtistsByStartingChar(artist_songs_list, starting_char):
    starting_char_upper = starting_char.upper()
    starting_char_lower = starting_char.lower()
    return [x for x in artist_songs_list if x[0][0] == starting_char_upper or x[0][0] == starting_char_lower]

def getArtistsSongsLengths(list_val):
    lengths = []
    artists = []
    songs = []
    for tuple_val in list_val:
        artists.append(tuple_val[0])
        songs.append(tuple_val[1])
        lengths.append(len(tuple_val[1]))
    return (artists, songs, lengths)