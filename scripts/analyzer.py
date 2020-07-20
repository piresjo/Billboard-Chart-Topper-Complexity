import lyricsgenius
import time
import json
import re
import extractor
import enchant
from nltk.tokenize import sent_tokenize, word_tokenize

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

    def notPunctuation(word):
        return not (len(word) == 1 and (not word.isalpha()))

    def getNumSyllables(l):
        return len(filter(lambda s: isdigit(s.encode('ascii', 'ignore').lower()[-1]), l))

    def numSyllables(word):
        prondict = cmudict.dict()
        numsyllables_pronlist = lambda l: len(filter(lambda s: isdigit(s.encode('ascii', 'ignore').lower()[-1]), l))
        try:
            return list(set(map(numsyllables_pronlist, prondict[word.lower()])))
        except KeyError:
            return [0]

    def textStatistics(text):
        word_count = get_word_count(text)
        sent_count = get_sent_count(text)
        syllable_count = sum(map(lambda w: max(numSyllables(w)), word_tokenize(text)))
        return word_count, sent_count, syllable_count

    def fleschKincaid(self, songLyrics):
        get_word_count = lambda text: len(filter(notNunctuation, word_tokenize(text)))
        get_sent_count = lambda text: len(sent_tokenize(text))
        word_count, sent_count, syllable_count = textStatistics(text)
        return (0.39 * (word_count / sent_count)) + (11.8 * (syllable_count / word_count)) - 15.59



analyzer = Analyzer()
analyzer.setupForArtist("Tame Impala", "Lyrics_TameImpala.json")
print(analyzer.lyric_dict)
analyzer.countUniqueWords(analyzer.lyric_dict)

