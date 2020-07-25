from flask import Flask, render_template, url_for
from siteUtils import *
import json

app = Flask(__name__)
data_file_location = 'static/data/combinedArtistsAndSongs.json' 
site = SiteObject()

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/hot100')
def hot100():
    if site.artists_and_songs is None:
        with open(data_file_location, 'r') as json_file:
            artists_and_songs = json.load(json_file)
        site.artists_and_songs = artists_and_songs
    lists = getArtistsSongsLengths(site.artists_and_songs)
    return render_template('hot100.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2])

@app.route('/hot100/a')
def hot100StartWithA():
    if site.artists_and_songs is None:
        with open(data_file_location, 'r') as json_file:
            artists_and_songs = json.load(json_file)
        site.artists_and_songs = artists_and_songs
    if 'A' not in site.artists_by_letter_dict:
        sorted_final_list = getArtistsByStartingChar(artists_and_songs, 'a')
        site.artists_by_letter_dict['A'] = sorted_final_list
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['A'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='A')

@app.route('/hot100/b')
def hot100StartWithB():
    if site.artists_and_songs is None:
        with open(data_file_location, 'r') as json_file:
            artists_and_songs = json.load(json_file)
        site.artists_and_songs = artists_and_songs
    if 'A' not in site.artists_by_letter_dict:
        sorted_final_list = getArtistsByStartingChar(artists_and_songs, 'b')
        site.artists_by_letter_dict['B'] = sorted_final_list
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['B'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='B')
