import lyricsgenius
import time
import json
import re
import sys
import os.path
from config import AccessToken

class Extractor:
    def __init__(self, verbose=False, remove=True, skip=True, excluded=["(Remix)", "(Live)"]):
        self.genius = self.setupGenius(verbose, remove, skip, excluded)
        self.artist = None
        self.songs_dict = None

    def setupGenius(self, verbose, remove, skip, excluded):
        self.genius = lyricsgenius.Genius(AccessToken)
        self.genius.verbose = verbose
        self.genius.remove_section_headers = remove
        self.genius.skip_non_songs = skip
        self.genius.excluded_terms = excluded
        return self.genius

    def saveLyricsFromArtist(self, artist, max_songs=300, sort="title"):
        artist_object = self.genius.search_artist(artist, max_songs, sort)
        self.artist = artist_object
        self.artist.save_lyrics()
        self.songs_dict = None

    def extractFromFile(self, file_name_val=None):
        if file_name_val is None:
            new_name = self.artist.name.replace(" ", "")
            file_name = 'Lyrics_' + new_name + '.json'
        else:
            file_name = file_name_val
        self.songs_dict = {}

        with open(file_name) as json_file:
            data = json.load(json_file)
            songs_array = data['songs']
            for song in songs_array:
                title_val = song['title']
                lyric_val = song['lyrics']
                if lyric_val == '[Instrumental]':
                    continue
                single_line_lyrics = re.sub("[\(\[].*?[\)\]]", "", lyric_val)
                single_line_lyrics = single_line_lyrics.replace('\n\n', ' ')
                single_line_lyrics = single_line_lyrics.replace('\n', ' ')
                single_line_lyrics = single_line_lyrics.replace('.', '')
                single_line_lyrics = single_line_lyrics.replace(',', '')
                self.songs_dict[title_val] = single_line_lyrics.split()

if len(sys.argv) < 2:
    print("Need A Flag. Either Choose '-f' To Generate Extractor From File, Or '-a' To Generate With An Artist.")
    exit()
if len(sys.argv) < 3:
    print("Need either a file name or artist")
    exit()
if sys.argv[1] != '-f' and sys.argv[1] != '-a':
    print("Incorrect Flag. Either Choose '-f' To Generate Extractor From File, Or '-a' To Generate With An Artist.")
    exit()

start_time = time.time()
extractor = Extractor()

if sys.argv[1] == '-f':
    if os.path.isfile(sys.argv[2]):
        extractor.extractFromFile(sys.argv[2])

if sys.argv[1] == '-a':
    extractor.saveLyricsFromArtist(sys.argv[2])

print(extractor.songs_dict)
print(time.time() - start_time)




