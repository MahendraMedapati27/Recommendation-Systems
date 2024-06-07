import pandas as pd
import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Load the data
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
movie2idx = pickle.load(open('index.pkl', 'rb'))
X = pickle.load(open('similarity.pkl', 'rb'))

# Define the recommendation function
def recommend(movie):
    idx = movie2idx[f'{movie}']
    query = X[idx]
    query = query.toarray()
    scores = cosine_similarity(query, X)
    scores = scores.flatten()
    recommended_idx = (-scores).argsort()[1:11]  # Get top 10 recommendations
    recommended_movies = movies['title'].iloc[recommended_idx]
    return recommended_movies

# Define the function to get movie poster
def get_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=72a9d9323a2c440408058948d9e40fea')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Streamlit app
st.title('Movie Recommendation System')

# Initialize selected movie name
selected_movie_name = st.selectbox(
    'Enter the Movie Name',
    movies['title'].values
)

if st.button('Recommend'):
    movie_names = recommend(selected_movie_name)
    
    # First row
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            movie_name = movie_names.iloc[i]
            recommended_index = movies[movies['title'] == movie_name]['movie_id'].values[0]
            poster_url = get_poster(recommended_index)
            st.image(poster_url, caption=movie_name, use_column_width=True, output_format='PNG')

    # Second row
    cols = st.columns(5)
    for i in range(5, 10):
        with cols[i - 5]:
            movie_name = movie_names.iloc[i]
            recommended_index = movies[movies['title'] == movie_name]['movie_id'].values[0]
            poster_url = get_poster(recommended_index)
            st.image(poster_url, caption=movie_name, use_column_width=True, output_format='PNG')

