import json
import os
import billboard
import datetime
import time

#For now, just have the past five weeks
#TODO: If there are artists with 'featuring', should we split the artists?

class BillboardExtractor:
    def __init__(self, start_date=None, end_date=None):
        self.start_date = start_date
        self.end_date = end_date
        self.unique_songs = set()
        self.artists = set()
        self.unique_artists = set()
        self.charts = {}
        self.artists_and_songs = {}

    def extractCharts(self):
        chart_val = billboard.ChartData('hot-100')
        date = datetime.date.today()
        week_delta = datetime.timedelta(7)
        temp_count = 0
        while chart_val is not None:
            if temp_count == 5:
                return
            self.charts[str(date)] = chart_val
            date = date - week_delta
            chart_val = billboard.ChartData('hot-100', str(date))
            temp_count += 1

    def getArtistsAndSongs(self):
        for chart_date in self.charts.keys():
            song_list = self.charts[chart_date]
            for song in song_list:
                self.artists.add(song.artist)
                self.unique_songs.add(song.title)
                if song.artist not in self.artists_and_songs:
                    self.artists_and_songs[song.artist] = set([song.title])
                else:
                    self.artists_and_songs[song.artist].add(song.title)

    def writeToFile(self):
        for artist in self.artists_and_songs.keys():
            self.artists_and_songs[artist] = list(self.artists_and_songs[artist])
        with open('artistsAndSongs.json', 'w') as outfile:
            json.dump(self.artists_and_songs, outfile)

startTime = time.time()
billboardExtractor = BillboardExtractor()
billboardExtractor.extractCharts()
billboardExtractor.getArtistsAndSongs()
billboardExtractor.writeToFile()


'''
    Use for testing
'''
#print(billboardExtractor.charts)
#print(billboardExtractor.charts['2020-06-28'])
#print(billboardExtractor.artists)
#print(billboardExtractor.artists_and_songs)
