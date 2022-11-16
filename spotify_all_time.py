import json
import csv
from pathlib import Path

path = r"C:\Users\Eric\Desktop\Datasets\Spotify Data\my_spotify_data\MyData\endsong_1.json"
path1 = r"C:\Users\Eric\Desktop\Datasets\Spotify Data\my_spotify_data\MyData\endsong_0.json"
track = 'master_metadata_track_name'
artist = 'master_metadata_album_artist_name'

pat = Path(r"C:\Users\Eric\Desktop\Datasets\Spotify Data\my_spotify_data\MyData")
this_list = []
for i in pat.glob('endsong_?.json'):
    with open(i, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
        for i, j in enumerate(data):
            this_list.append(data[i])
    


# with open(path, 'r', encoding='utf-8') as f:
#     data = json.load(f)


# #initialize datastructures
# this_list = [data[i] for i,j in enumerate(data)]
new_dict = {}
final_dict = [{}]
x = map(lambda x:x[track], final_dict)
#append 
for i,j in enumerate(this_list):
    if j[artist] and j[track] in new_dict.values():
        for i,c in enumerate(final_dict):
            if j[artist]+' | '+j[track] in final_dict[i].keys():
                final_dict[i][j[artist]+' | '+j[track]] += j['ms_played']  
    else:
        new_dict.setdefault(str(i)+' '+ artist, j[artist]) #append into new_dict
        new_dict.setdefault(str(i)+' '+ track, j[track])
        final_dict[len(final_dict)-1] = {str(j[artist])+' | '+str(j[track]):j['ms_played']}
        final_dict.append({})

organized = sorted(final_dict, key=lambda x:list(x.values()), reverse=True)

with open('spotify_all_time3.csv', 'w', encoding='utf-8') as f:
    for i in organized:
        f.write(str(*i.items()))
        f.write('\n')