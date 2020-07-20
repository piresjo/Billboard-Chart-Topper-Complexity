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
        self.songs_tokens_dict = None
        self.songs_text_dict = None
        self.filtered_dict = None

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

    def extractFromFile(self, file_name_val=None):
        if file_name_val is None:
            new_name = self.artist.name.replace(" ", "")
            file_name = 'Lyrics_' + new_name + '.json'
        else:
            file_name = file_name_val
        self.songs_tokens_dict = {}
        self.songs_text_dict = {}

        with open(file_name) as json_file:
            data = json.load(json_file)
            songs_array = data['songs']
            for song in songs_array:
                title_val = song['title']
                lyric_val = song['lyrics']
                if lyric_val == '[Instrumental]':
                    continue
                lyrics = re.sub("[\(\[].*?[\)\]]", "", lyric_val)
                self.songs_text_dict[title_val] = lyrics.replace('\n\n', ' ').replace('\n', ' ')
            
                token_lyrics = re.sub("[\(\[].*?[\)\]]", "", lyric_val)
                token_lyrics = token_lyrics.replace('\n\n', ' ')
                token_lyrics = token_lyrics.replace('\n', ' ')
                token_lyrics = token_lyrics.replace('.', '')
                token_lyrics = token_lyrics.replace(',', '')
                self.songs_tokens_dict[title_val] = token_lyrics.split()

    def filterSongs(self):
        if self.songs_tokens_dict is None:
            return
        self.filtered_dict = {}
        for songTitle in self.songs_tokens_dict.keys():
            if len(self.songs_tokens_dict[songTitle]) != 0:
                self.filtered_dict[songTitle] = self.songs_tokens_dict[songTitle]


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
        extractor.filterSongs()

if sys.argv[1] == '-a':
    extractor.saveLyricsFromArtist(sys.argv[2])

'''
    For testing
'''
#print(extractor.songs_tokens_dict)
#print("")
#print(extractor.songs_text_dict)
#print(len(extractor.filtered_dict))
#print(time.time() - start_time)




