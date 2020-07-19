import json
import os
import billboard
import datetime
import time

#For now, just have the past five weeks
#TODO: If there are artists with 'featuring', should we split the artists?

class BillboardExtractor:
    def __init__(self, start_date=None, end_date=None):
        self.startDate = start_date
        self.endDate = end_date
        self.uniqueSongs = set()
        self.artists = set()
        self.uniqueArtists = set()
        self.charts = {}
        self.artistsAndSongs = {}

    def extractCharts(self):
        chartVal = billboard.ChartData('hot-100')
        date = datetime.date.today()
        weekDelta = datetime.timedelta(7)
        tempCount = 0
        while chartVal is not None:
            if tempCount == 5:
                return
            self.charts[str(date)] = chartVal
            date = date - weekDelta
            chartVal = billboard.ChartData('hot-100', str(date))
            tempCount += 1

    def getArtistsAndSongs(self):
        for chartDate in self.charts.keys():
            songList = self.charts[chartDate]
            for song in songList:
                self.artists.add(song.artist)
                self.uniqueSongs.add(song.title)
                if song.artist not in self.artistsAndSongs:
                    self.artistsAndSongs[song.artist] = set([song.title])
                else:
                    self.artistsAndSongs[song.artist].add(song.title)

    def writeToFile(self):
        for artist in self.artistsAndSongs.keys():
            self.artistsAndSongs[artist] = list(self.artistsAndSongs[artist])
        with open('artistsAndSongs.json', 'w') as outfile:
            json.dump(self.artistsAndSongs, outfile)

startTime = time.time()
billboardExtractor = BillboardExtractor()
billboardExtractor.extractCharts()
billboardExtractor.getArtistsAndSongs()
billboardExtractor.writeToFile()


'''
    Use for testing
'''
#print(billboardExtractor.charts)
#print(billboardExtractor.charts['2020-06-27'])
#print(billboardExtractor.artists)
#print(billboardExtractor.artistsAndSongs)
