import lyricsgenius
import time
import json
import re
import extractor
import enchant

class Analyzer:
    def __init__(self):
        self.extractor = extractor.Extractor()
        self.dictionary = enchant.Dict("en_US")
        self.lyric_dict = None

    def setupForArtist(self, artist_name, file_name=None):
        if file_name is None:
            self.extractor.saveLyricsFromArtist(artist_name)
            self.extractor.extractFromFile()
        else:
            self.extractor.extractFromFile(file_name)
        self.lyric_dict = self.extractor.songs_dict

    def countUniqueWords(self, lyric_dict):
        giant_lyric_list = [x for y in list(lyric_dict.values()) for x in y]
        unique_words = list(set(giant_lyric_list))
        print(len(unique_words))

analyzer = Analyzer()
analyzer.setupForArtist("Tame Impala", "Lyrics_TameImpala.json")
print(analyzer.lyric_dict)
analyzer.countUniqueWords(analyzer.lyric_dict)

