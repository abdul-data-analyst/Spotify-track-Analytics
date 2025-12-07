from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import re

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='e86decbdb344499482b9f4e95c617f52',
    client_secret='296cc83829544661b87faef4b46f1bae'
))

#MySQL database connection
db_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : 'root',
    'database' : 'spotify_db'
}

#connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

#Full track url
track_url = "https://open.spotify.com/track/13wIQbwSuQ4YFvDvtQgSVc"

#Extract track ID directly from track_url
track_id = re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)

track = sp.track(track_id)

#Extract Metadata
track_data = {
    'Track Name' : track['name'],
    'Artist' : track['artists'][0]['name'],
    'Album' : track['album']['name'],
    'Popularity' : track['popularity'],
    'Duration (minutes)' :track['duration_ms'] / 60000
}

#insert data into MySQL
insert_query = """
INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
VALUES (%s, %s, %s, %s, %s)
"""
cursor.execute(insert_query,(
    track_data['Track Name'],
    track_data['Artist'],
    track_data['Album'],
    track_data['Popularity'],
    track_data['Duration (minutes)']
))
connection.commit()

print(f"Track '{track_data['Track Name']}' by {track_data['Artist']} inserted into the database.")

#close the conection
cursor.close()
connection.close()