from flask import Flask, render_template, url_for
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/hot100')
def hot100():
    with open('combinedArtistsAndSongs.json', 'r') as json_file:
        artistsAndSongs = json.load(json_file)
    artists = list(artistsAndSongs.keys())
    lengths = []
    for artist in artists:
        artistsAndSongs[artist] = sorted(artistsAndSongs[artist])
        lengths.append(len(artistsAndSongs[artist]))
    songs = list(artistsAndSongs.values())
    return render_template('hot100.html', artists=artists, songs=songs, length=len(artists), lengths=lengths)