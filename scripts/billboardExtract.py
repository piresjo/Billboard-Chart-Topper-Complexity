import json
import os
import billboard
import datetime
import time
import sys

#For now, just have the past five weeks
#TODO: If there are artists with 'featuring', should we split the artists?

class BillboardExtractor:
    def __init__(self, date):
        self.start_date = date
        self.unique_songs = set()
        self.artists = set()
        self.unique_artists = set()
        self.charts = {}
        self.artists_and_songs = {}

    def extractCharts(self, number_of_weeks=100):
        chart_date = datetime.datetime.strptime(self.start_date, '%Y-%m-%d').date()
        try:
            chart_val = billboard.ChartData('hot-100', self.start_date)
            week_delta = datetime.timedelta(7)
            first_date = datetime.date(1954, 8, 4)
            while chart_date >= first_date and number_of_weeks != 0:
                print(chart_val.date)
                self.charts[chart_val.date] = chart_val
                chart_date = chart_date - week_delta
                chart_val = billboard.ChartData('hot-100', str(chart_date))
                number_of_weeks -= 1
        except:
            print("Timeout error at date " + str(chart_date))
            return

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
        with open('artistsAndSongs' + self.start_date + '.json', 'w') as outfile:
            json.dump(self.artists_and_songs, outfile)

if len(sys.argv) < 2:
    print("Need A Date")
    exit()

start_time = time.time()
billboard_extractor = BillboardExtractor(sys.argv[1])
billboard_extractor.extractCharts()
billboard_extractor.getArtistsAndSongs()
billboard_extractor.writeToFile()
print(time.time() - start_time)


'''
    Use for testing
'''
#print(billboard_extractor.charts)
#print(billboard_extractor.charts['2020-07-25'])
#print(billboard_extractor.artists)
#print(billboard_extractor.artists_and_songs)
