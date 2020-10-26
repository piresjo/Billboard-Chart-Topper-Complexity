import json
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
        self.artists_songs_weeks_on_chart = {}

    def extractCharts(self, number_of_weeks=100):
        chart_date = datetime.datetime.strptime(self.start_date, '%Y-%m-%d').date()
        try:
            chart_val = billboard.ChartData('hot-100', date=self.start_date, timeout=20)
            week_delta = datetime.timedelta(7)
            first_date = datetime.date(1954, 8, 4)
            while chart_date >= first_date and number_of_weeks != 0:
                print(chart_val.date)
                self.charts[chart_val.date] = chart_val[0:40]
                chart_date = chart_date - week_delta
                chart_val = billboard.ChartData('hot-100', str(chart_date))
                number_of_weeks -= 1
        except:
            print("Timeout error at date " + str(chart_date))
            return

    def getArtistsAndSongs(self):
        for chart_date in self.charts.keys():
            song_list = self.charts[chart_date]
            for i in range(0, len(song_list)):
                if song_list[i].artist in self.artists_songs_weeks_on_chart:
                    if song_list[i].title in self.artists_songs_weeks_on_chart[song_list[i].artist]:
                        self.artists_songs_weeks_on_chart[song_list[i].artist][song_list[i].title]["length"] += 1
                        if self.artists_songs_weeks_on_chart[song_list[i].artist][song_list[i].title]["top"] > i + 1:
                            self.artists_songs_weeks_on_chart[song_list[i].artist][song_list[i].title]["top"] = i + 1
                    else:
                        self.artists_songs_weeks_on_chart[song_list[i].artist][song_list[i].title] = {}
                        self.artists_songs_weeks_on_chart[song_list[i].artist][song_list[i].title]["length"] = 1
                        self.artists_songs_weeks_on_chart[song_list[i].artist][song_list[i].title]["top"] = i + 1
                else:
                    self.artists_songs_weeks_on_chart[song_list[i].artist] = {}
                    self.artists_songs_weeks_on_chart[song_list[i].artist][song_list[i].title] = {}
                    self.artists_songs_weeks_on_chart[song_list[i].artist][song_list[i].title]["length"] = 1
                    self.artists_songs_weeks_on_chart[song_list[i].artist][song_list[i].title]["top"] = i + 1
                

    def writeToFile(self):
        with open('artistsAndSongs' + self.start_date + '.json', 'w') as outfile:
            json.dump(self.artists_songs_weeks_on_chart, outfile)

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
