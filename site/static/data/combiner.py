from os import listdir
from os.path import isfile, join
import json

mypath = "/Users/joe/Documents/GitHub/Billboard-Chart-Topper-Complexity/site/static/data"
files = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".json")]
combined_dict = {}

for filename in files:
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        for artist in data.keys():
            if artist not in combined_dict:
                combined_dict[artist] = data[artist]
            else:
                for song in data[artist]:
                    if song not in combined_dict[artist]:
                        combined_dict[artist][song] = data[artist][song]
                    else:
                        combined_dict[artist][song]['length'] += data[artist][song]['length']
                        if combined_dict[artist][song]['top'] > data[artist][song]['top']:
                            combined_dict[artist][song]['top'] = data[artist][song]['top']


sort_list = []
for artist in combined_dict.keys():
    sort_list.append([artist, combined_dict[artist]])
    sort_list = sorted(sort_list, key=lambda x: x[0])

with open('combinedArtistsAndSongs.json', 'w') as outfile:
    json.dump(sort_list, outfile)
