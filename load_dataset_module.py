#import the required libraries
import numpy as np
import csv
from itertools import islice



def retrieve_artist_features():
    artist_music = {} #define an empty dict to store the data
    
    #open and read the file using csv reader
    with open('data.csv', encoding='utf8') as file:
        data = csv.reader(file)
        #start reading the file from the second line
        for row in islice(data, 1, None):
            #save each data row as a dict using the ID as the key and the values being the details
            artist_music[row[6]] = {'artists': row[1],
                                 'key': int(row[8]),
                                 'popularity': int(row[13]),
                                 'year': int(row[18])}
    #return the dict with all the data in it
    return artist_music



def retrieve_music_features():
    music_features = {} #define an empty dict to store the data
    
    #open and read the file using csv reader
    with open('data.csv', encoding='utf8') as file:
        data = csv.reader(file)
        #start reading the file from the second line
        for row in islice(data, 1, None):
            #save each data row as a dict using the ID as the key and the values being the details
            music_features[row[6]] = {'acousticness': float(row[0]),
                                   'danceability': float(row[2]),
                                   'duration_ms': int(row[3]),
                                   'energy': float(row[4]),
                                   'explicit': int(row[5]),
                                   'instrumentalness': float(row[7]),
                                   'key': int(row[8]),
                                   'liveness': float(row[9]),
                                   'loudness': float(row[10]),
                                   'mode': int(row[11]),
                                   'name': row[12],
                                   'popularity': int(row[13]),
                                   'release_date': row[14],
                                   'speechiness': float(row[15]),
                                   'tempo': float(row[16]),
                                   'valence': float(row[17])}
    #return the dict with all the data in it
    return music_features