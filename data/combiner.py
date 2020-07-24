from os import listdir
from os.path import isfile, join
import json

mypath = "/Users/joe/Documents/GitHub/Billboard-Chart-Topper-Complexity/data"
files = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".json")]
combined_dict = {}

for filename in files:
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        for artist in data.keys():
            if artist not in combined_dict:
                combined_dict[artist] = set(data[artist])
            else:
                combined_dict[artist].update(data[artist])

for artist in combined_dict.keys():
    combined_dict[artist] = list(combined_dict[artist])

with open('combinedArtistsAndSongs.json', 'w') as outfile:
    json.dump(combined_dict, outfile)
