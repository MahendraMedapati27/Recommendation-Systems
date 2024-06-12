import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import requests
import base64

CLIENT_ID = "af23beaea3074746a381796e42d53387"
CLIENT_SECRET = "2de2db11d9e74195893a40a8424b6203"

# Function to refresh the Spotify token
def refresh_token():
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()
    response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={'grant_type': 'client_credentials'},
        headers={'Authorization': f'Basic {b64_auth_str}'}
    )
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        st.error("Failed to refresh Spotify token")
        return None

# Initialize the Spotify client
access_token = refresh_token()
sp = spotipy.Spotify(auth=access_token)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        album_cover_url = get_song_album_cover_url(music.iloc[i[0]].song, artist)
        # Retry with a refreshed token if the first attempt fails
        if album_cover_url == "https://i.postimg.cc/0QNxYz4V/social.png":
            new_access_token = refresh_token()
            sp.auth = new_access_token
            album_cover_url = get_song_album_cover_url(music.iloc[i[0]].song, artist)
        recommended_music_posters.append(album_cover_url)
        recommended_music_names.append(music.iloc[i[0]].song)

    return recommended_music_names, recommended_music_posters

st.header('Music Recommender System')
music = pickle.load(open(r'C:\Users\Hp\OneDrive\Desktop\MRS\Song_Recommendation\df.pkl','rb'))
similarity = pickle.load(open(r'C:\Users\Hp\OneDrive\Desktop\MRS\Song_Recommendation\similarity.pkl','rb'))

music_list = music['song'].values
selected_movie = st.selectbox(
    "Type or select a song from the dropdown of 8000 songs",
    music_list
)

if st.button('Recommend'):
    recommended_music_names, recommended_music_posters = recommend(selected_movie)
    
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            movie_name = recommended_music_names[i]
            poster_url = recommended_music_posters[i]
            st.image(poster_url, caption=movie_name, use_column_width=True)
