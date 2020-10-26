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
    site.processLetter('a')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['A'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='A')

@app.route('/hot100/b')
def hot100StartWithB():
    site.processLetter('b')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['B'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='B')

@app.route('/hot100/c')
def hot100StartWithC():
    site.processLetter('c')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['C'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='C')

@app.route('/hot100/d')
def hot100StartWithD():
    site.processLetter('d')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['D'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='D')

@app.route('/hot100/e')
def hot100StartWithE():
    site.processLetter('e')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['E'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='E')

@app.route('/hot100/f')
def hot100StartWithF():
    site.processLetter('f')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['F'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='F')

@app.route('/hot100/g')
def hot100StartWithG():
    site.processLetter('g')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['G'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='G')

@app.route('/hot100/h')
def hot100StartWithH():
    site.processLetter('h')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['H'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='H')

@app.route('/hot100/i')
def hot100StartWithI():
    site.processLetter('i')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['I'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='I')

@app.route('/hot100/j')
def hot100StartWithJ():
    site.processLetter('j')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['J'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='J')

@app.route('/hot100/k')
def hot100StartWithK():
    site.processLetter('k')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['K'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='K')

@app.route('/hot100/l')
def hot100StartWithL():
    site.processLetter('l')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['L'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='L')

@app.route('/hot100/m')
def hot100StartWithM():
    site.processLetter('m')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['M'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='M')

@app.route('/hot100/n')
def hot100StartWithN():
    site.processLetter('n')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['N'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='N')

@app.route('/hot100/o')
def hot100StartWithO():
    site.processLetter('o')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['O'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='O')

@app.route('/hot100/p')
def hot100StartWithP():
    site.processLetter('p')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['P'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='P')

@app.route('/hot100/q')
def hot100StartWithQ():
    site.processLetter('q')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['Q'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='Q')

@app.route('/hot100/r')
def hot100StartWithR():
    site.processLetter('r')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['R'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='R')

@app.route('/hot100/s')
def hot100StartWithS():
    site.processLetter('s')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['S'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='S')

@app.route('/hot100/t')
def hot100StartWithT():
    site.processLetter('t')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['T'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='T')

@app.route('/hot100/u')
def hot100StartWithU():
    site.processLetter('u')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['U'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='U')

@app.route('/hot100/v')
def hot100StartWithV():
    site.processLetter('v')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['V'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='V')

@app.route('/hot100/w')
def hot100StartWithW():
    site.processLetter('w')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['W'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='W')

@app.route('/hot100/x')
def hot100StartWithX():
    site.processLetter('x')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['X'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='X')

@app.route('/hot100/y')
def hot100StartWithY():
    site.processLetter('y')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['Y'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='Y')

@app.route('/hot100/z')
def hot100StartWithZ():
    site.processLetter('z')
    lists = getArtistsSongsLengths(site.artists_by_letter_dict['Z'])
    return render_template('hot100ByLetter.html', artists=lists[0], songs=lists[1], length=len(lists[0]), lengths=lists[2], starting_char='Z')



