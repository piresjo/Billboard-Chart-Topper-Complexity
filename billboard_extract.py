import json
import os
import billboard
import datetime

class BillboardExtractor:
    def __init__(self, start_date=None, end_date=None):
        self.start_date = start_date
        self.end_date = end_date
        self.unique_songs = Set()
        self.unique_artists = Set()
        self.charts = {}

    def extractCharts(self):
        chart_val = billboard.ChartData('hot-100')
        date = datetime.date.today()
        while chart_val is not None:
            self.charts[str(date)] = chart_val
            date.replace(day=day-7)
            chart_val = billboard.ChartData('hot-100', str(date))

    def getUniqueSongsAndArtists(self):
        for date, chart in charts:
            for song in chart:
                self.unique_songs.add(song.title)
                self.unique_artists.add(song.artist)
