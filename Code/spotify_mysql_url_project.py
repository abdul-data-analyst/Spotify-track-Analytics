from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import re


# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id= 'e86decbdb344499482b9f4e95c617f52',
    client_secret= '296cc83829544661b87faef4b46f1bae'
))


# MySQL Database Connection
db_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : 'root',
    'database' : 'spotify_db'
}

#connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Read track URLs from files.
file_path = "track_url"
with open(file_path, 'r') as file:
    track_url = file.readlines()

# Process each URL
for track_url in track_url:
    track_url = track_url.strip()
    try:
        # Extract track ID from url
        track_id = re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)

        #fetch track details from spotify API
        track = sp.track(track_id)

        #Extract Metadata
        track_data = {
            'Track Name': track['name'],
            'Artist': track['artists'][0]['name'],
            'Album': track['album']['name'],
            'Popularity': track['popularity'],
            'Duration (minutes)': track['duration_ms'] / 60000
        }

        #insert data into mysql
        insert_query ="""
        INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            track_data['Track Name'],
            track_data['Artist'],
            track_data['Album'],
            track_data['Popularity'],
            track_data['Duration (minutes)']
        ))
        connection.commit()

        print(f"Inserted : {track_data['Track Name']} by {track_data['Artist']}")

    except Exception as e:
        print(f"Error processing URL: {track_url}, Error: {e}")

#close connection
cursor.close()
connection.close()

print("All tracks have been processed and  inserted into the database")


